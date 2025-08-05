import logging
import joblib
import pandas as pd
import shap
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
import tempfile
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Breast Cancer Classification API", version="1.0.0")
templates = Jinja2Templates(directory="app/templates")

# Pydantic models
class PredictionRequest(BaseModel):
    features: list[float]
    patient_name: str = "Unknown Patient"


class Factor(BaseModel):
    name: str
    impact: float
    direction: str


class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    probability_benign: float
    probability_malignant: float
    contributing_factors: list[Factor]
    patient_name: str


# Global variables
model, scaler, feature_selector, explainer = None, None, None, None
feature_names, selected_feature_names = None, None


@app.on_event("startup")
async def load_models():
    """Load models and derive feature names from the artifacts themselves."""
    global model, scaler, feature_selector, explainer, feature_names, selected_feature_names

    logger.info("Starting Breast Cancer Classification API...")
    try:
        # Load all artifacts first
        model = joblib.load("models/breast_cancer_model.pkl")
        scaler = joblib.load("models/scaler.pkl")
        feature_selector = joblib.load("models/feature_selector.pkl")
        raw_background_data = pd.read_csv("models/shap_background.csv")
        logger.info("Models and raw background data loaded successfully.")

        # The source of truth for the 30 original feature names is the selector itself.
        feature_names = feature_selector.feature_names_in_.tolist()
        logger.info(f"Retrieved {len(feature_names)} original feature names from feature selector artifact.")

        # Now, get the 15 selected feature names. This will now work without error.
        selected_feature_names = feature_selector.get_feature_names_out(input_features=feature_names)
        logger.info(f"Retrieved {len(selected_feature_names)} selected feature names.")

        # The background data already contains only the selected features, so we use it directly
        # No need to select columns since the background data is already in the correct format
        logger.info("Using background data with selected features directly...")

        # Initialize the explainer with the background data as-is (it's already preprocessed)
        explainer = shap.KernelExplainer(model.predict_proba, raw_background_data)
        logger.info("SHAP explainer created successfully with preprocessed background data.")

        logger.info("API startup completed.")

    except Exception as e:
        logger.error(f"Error during startup: {e}", exc_info=True)
        raise


@app.post("/predict", response_model=PredictionResponse)
async def predict(input_data: PredictionRequest):
    """Make a single prediction."""
    try:
        if len(input_data.features) != len(feature_names):
            raise HTTPException(
                status_code=400,
                detail=f"Expected {len(feature_names)} features, got {len(input_data.features)}"
            )

        features_df = pd.DataFrame([input_data.features], columns=feature_names)

        # This pipeline is correct.
        features_scaled_np = scaler.transform(features_df)
        features_scaled_df = pd.DataFrame(features_scaled_np, columns=feature_names)
        features_selected_np = feature_selector.transform(features_scaled_df)
        final_features_df = pd.DataFrame(features_selected_np, columns=selected_feature_names)

        prediction_proba = model.predict_proba(final_features_df)[0]
        prediction = int(model.predict(final_features_df)[0])

        confidence = float(max(prediction_proba))
        prediction_str = "malignant" if prediction == 1 else "benign"

        top_factors = []
        try:
            # Get SHAP values
            shap_values = explainer.shap_values(final_features_df)

            # Handle different SHAP output formats and ensure we get the right values
            if isinstance(shap_values, list):
                # For binary classification, shap_values is a list with 2 elements
                # Use the prediction class (0 or 1)
                shap_values_for_prediction = shap_values[prediction][0]
            else:
                # Single array case
                shap_values_for_prediction = shap_values[0]

            # Convert to numpy array and ensure it's 1D
            shap_values_for_prediction = np.array(shap_values_for_prediction).flatten()

            # Create feature importance list with proper scalar values
            feature_importance = []
            for i, feature_name in enumerate(final_features_df.columns):
                importance = float(shap_values_for_prediction[i])
                feature_importance.append((feature_name, importance))

            # Sort by absolute importance
            feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)

            for feature_name, importance in feature_importance[:5]:
                if prediction == 1:
                    direction = "increases risk" if importance > 0 else "decreases risk"
                else:  # benign
                    direction = "decreases risk" if importance > 0 else "increases risk"

                top_factors.append(Factor(
                    name=feature_name.replace("_", " ").title(),
                    impact=float(abs(importance)),
                    direction=direction
                ))
            logger.info("SHAP explanation generated successfully.")

        except Exception as shap_error:
            logger.warning(f"SHAP explanation failed: {shap_error}", exc_info=True)
            top_factors = []

        logger.info(f"Prediction made: {prediction_str} (confidence: {confidence:.3f})")

        return PredictionResponse(
            prediction=prediction_str,
            confidence=confidence,
            probability_benign=float(prediction_proba[0]),
            probability_malignant=float(prediction_proba[1]),
            contributing_factors=top_factors,
            patient_name=input_data.patient_name
        )

    except Exception as e:
        logger.error(f"Prediction error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal error occurred during prediction.")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate-pdf")
async def generate_pdf(input_data: PredictionRequest):
    """Generate a PDF report for the prediction."""
    try:
        if len(input_data.features) != len(feature_names):
            raise HTTPException(
                status_code=400,
                detail=f"Expected {len(feature_names)} features, got {len(input_data.features)}"
            )

        # Make the prediction first
        features_df = pd.DataFrame([input_data.features], columns=feature_names)
        features_scaled_np = scaler.transform(features_df)
        features_scaled_df = pd.DataFrame(features_scaled_np, columns=feature_names)
        features_selected_np = feature_selector.transform(features_scaled_df)
        final_features_df = pd.DataFrame(features_selected_np, columns=selected_feature_names)

        prediction_proba = model.predict_proba(final_features_df)[0]
        prediction = int(model.predict(final_features_df)[0])
        confidence = float(max(prediction_proba))
        prediction_str = "malignant" if prediction == 1 else "benign"

        # Get SHAP explanations
        top_factors = []
        try:
            shap_values = explainer.shap_values(final_features_df)

            if isinstance(shap_values, list):
                shap_values_for_prediction = shap_values[prediction][0]
            else:
                shap_values_for_prediction = shap_values[0]

            shap_values_for_prediction = np.array(shap_values_for_prediction).flatten()

            feature_importance = []
            for i, feature_name in enumerate(final_features_df.columns):
                importance = float(shap_values_for_prediction[i])
                feature_importance.append((feature_name, importance))

            feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)

            for feature_name, importance in feature_importance[:5]:
                if prediction == 1:
                    direction = "increases risk" if importance > 0 else "decreases risk"
                else:  # benign
                    direction = "decreases risk" if importance > 0 else "increases risk"

                top_factors.append({
                    "name": feature_name.replace("_", " ").title(),
                    "impact": float(abs(importance)),
                    "direction": direction
                })
        except Exception as shap_error:
            logger.warning(f"SHAP explanation failed: {shap_error}", exc_info=True)
            top_factors = []

        # Generate PDF
        pdf_path = generate_pdf_report(
            input_data.features,
            prediction_str,
            confidence,
            prediction_proba[0],
            prediction_proba[1],
            top_factors,
            feature_names,
            input_data.patient_name
        )

        return FileResponse(
            path=pdf_path,
            media_type='application/pdf',
            filename=f"breast_cancer_prediction_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{input_data.patient_name}.pdf"
        )

    except Exception as e:
        logger.error(f"PDF generation error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal error occurred during PDF generation.")


def generate_pdf_report(features, prediction, confidence, prob_benign, prob_malignant, contributing_factors, feature_names, patient_name):
    """Generate a PDF report for the prediction results."""

    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        pdf_path = tmp_file.name

    # Create the PDF document
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    story = []

    # Get styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.darkblue
    )

    normal_style = styles['Normal']

    # Title
    story.append(Paragraph("Breast Cancer Classification Report", title_style))
    story.append(Spacer(1, 20))

    # Patient Information
    story.append(Paragraph("Patient Information", heading_style))
    patient_data = [
        ["Patient Name", patient_name],
        ["Report Date", datetime.now().strftime('%B %d, %Y')],
        ["Report Time", datetime.now().strftime('%I:%M %p')]
    ]

    patient_table = Table(patient_data, colWidths=[2 * inch, 3 * inch])
    patient_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgreen),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ]))

    story.append(patient_table)
    story.append(Spacer(1, 20))

    # Date and time
    story.append(Paragraph(f"Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", normal_style))
    story.append(Spacer(1, 20))

    # Prediction Results
    story.append(Paragraph("Prediction Results", heading_style))

    # Create prediction table
    prediction_data = [
        ["Prediction", prediction.upper()],
        ["Confidence", f"{confidence:.1%}"],
        ["Probability (Benign)", f"{prob_benign:.1%}"],
        ["Probability (Malignant)", f"{prob_malignant:.1%}"]
    ]

    prediction_table = Table(prediction_data, colWidths=[2 * inch, 3 * inch])
    prediction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ]))

    story.append(prediction_table)
    story.append(Spacer(1, 20))

    # Contributing Factors
    if contributing_factors:
        story.append(Paragraph("Top Contributing Factors", heading_style))

        factors_data = [["Factor", "Impact", "Direction"]]
        for factor in contributing_factors:
            factors_data.append([
                factor["name"],
                f"{factor['impact']:.1%}",
                factor["direction"]
            ])

        factors_table = Table(factors_data, colWidths=[2 * inch, 1.5 * inch, 2 * inch])
        factors_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        story.append(factors_table)
        story.append(Spacer(1, 20))

    # Input Features
    story.append(Paragraph("Input Features", heading_style))

    # Create features table (showing first 10 features for brevity)
    features_data = [["Feature Name", "Value"]]
    for i, (name, value) in enumerate(zip(feature_names[:10], features[:10])):
        features_data.append([name.replace("_", " ").title(), f"{value:.4f}"])

    features_table = Table(features_data, colWidths=[3 * inch, 2 * inch])
    features_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    story.append(features_table)

    if len(features) > 10:
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"... and {len(features) - 10} more features", normal_style))

    story.append(Spacer(1, 20))

    # Disclaimer
    story.append(Paragraph("Disclaimer", heading_style))
    disclaimer_text = """
    <strong>⚠️ FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY</strong><br/><br/>
    This AI-powered diagnostic tool is designed for educational demonstrations and research purposes.
    <strong>It is NOT a certified medical device</strong> and should never be used for actual clinical diagnosis,
    patient treatment, or medical decision-making. The predictions are based on machine learning algorithms
    and are not a substitute for professional medical advice, diagnosis, or treatment.
    <strong>Always consult with qualified healthcare professionals for all medical decisions.</strong><br/><br/>
    <strong>Results Disclaimer:</strong> These results are generated by machine learning algorithms for educational purposes only.
    The accuracy and reliability of predictions may vary. This tool is not intended for clinical use and should not replace
    professional medical evaluation.
    """
    story.append(Paragraph(disclaimer_text, normal_style))

    # Build the PDF
    doc.build(story)

    return pdf_path


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)
    