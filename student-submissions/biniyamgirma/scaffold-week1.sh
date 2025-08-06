echo " starting to setup everything you need........."
mkdir 'week01(temprature-predictor)'
cd 'week01(temprature-predictor)'
touch README.md
echo "creating a requirements file......."
cat <<rec > requirements.txt
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
rec
echo "requirements file created"
echo "creating essential folders and files"
mkdir data notebooks src models visuals app
cd notebooks
touch eda.ipynb model_training.ipynb
cd ..
cd src
touch __init__.py preprocess.py train.py evaluate.py predict.py
cd ..
cd app
touch cli_predict.py
echo "essential files and folders created"
echo "done setting up all thing needed"



