import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import openai  # Add this import if you want to catch OpenAI-specific errors

# Load environment variables
load_dotenv()

def create_simple_agent():
    """Create a healthcare advice AI agent using OpenAI"""
    
    # Initialize the language model
    llm = OpenAI(temperature=0.7)
    
    # Create a custom prompt template for healthcare
    template = """
    You are a knowledgeable and responsible AI assistant specializing in healthcare advice.
    Answer the following question with clear, accurate, and safe information.
    If you are unsure or the question requires a medical professional, say so.

    Question: {question}

    Answer:"""
    
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )
    
    # Create the chain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    return chain

def main():
    """Main function to test the agent"""
    
    # Create the agent
    agent = create_simple_agent()
    
    # Test questions
    test_questions = [
        "What is generative AI?",
        "Explain the difference between supervised and unsupervised learning",
        "What are the main challenges in AI deployment?"
    ]
    
    print("🤖 Simple AI Agent Test\n")
    
    for i, question in enumerate(test_questions, 1):
        print(f"Question {i}: {question}")
        try:
            response = agent.run(question)
            print(f"Answer: {response}\n")
        except openai.error.RateLimitError:
            print("Error: You have exceeded your OpenAI API quota. Please check your usage and billing.\n")
        except openai.error.AuthenticationError:
            print("Error: Authentication failed. Please check your OpenAI API key.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
        
        print("-" * 50)

if __name__ == "__main__":
    main()