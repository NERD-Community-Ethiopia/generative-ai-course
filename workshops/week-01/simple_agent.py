import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_google_genai import GoogleGenerativeAI


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

def create_simple_agent():
    """Create a simple AI agent using OpenAI with LangChain 0.1+ style"""

    llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

    template = """
    You are a helpful AI assistant. Answer the following question:
    Question: {question}
    Answer:"""

    prompt = PromptTemplate.from_template(template)

    chain = prompt | llm  # New RunnableSequence
    return chain

def main():
    agent = create_simple_agent()

    test_questions = [
        "What is generative AI?",
        "Explain the difference between supervised and unsupervised learning",
        "What are the main challenges in AI deployment?"
    ]

    print("🤖 Simple AI Agent Test\n")

    for i, question in enumerate(test_questions, 1):
        print(f"Question {i}: {question}")
        try:
            response = agent.invoke({"question": question})
            print(f"Answer: {response}\n")
        except Exception as e:
            print(f"Error: {e}")
        print("-" * 83)

if __name__ == "__main__":
    main()

