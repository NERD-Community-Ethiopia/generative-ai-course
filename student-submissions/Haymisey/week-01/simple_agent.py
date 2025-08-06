"""
Simple AI Agent using LangChain and OpenAI

This module creates a basic AI agent that can answer questions using OpenAI's API.
It demonstrates the fundamental concepts of LangChain including LLM initialization,
prompt templates, and chain creation.
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

def create_simple_agent():
    """
    Create a simple AI agent using OpenAI
    
    Returns:
        LLMChain: A chain that can process questions and generate responses
    """
    
    # Initialize the language model with moderate creativity
    llm = OpenAI(temperature=0.7)
    
    # Create a prompt template for structured responses
    template = """
    You are a helpful AI assistant specialized in explaining technical concepts clearly.
    Please provide a comprehensive answer to the following question:
    
    Question: {question}
    
    Answer:"""
    
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )
    
    # Create the chain that combines the LLM and prompt
    chain = LLMChain(llm=llm, prompt=prompt)
    
    return chain

def test_agent(agent, questions):
    """
    Test the agent with a list of questions
    
    Args:
        agent: The LLMChain agent to test
        questions (list): List of questions to ask the agent
    """
    print("🤖 Simple AI Agent Test\n")
    
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        print("-" * 50)
        
        try:
            response = agent.run(question)
            print(f"Answer: {response}\n")
        except Exception as e:
            print(f"Error: {e}")
            print("This might be due to missing API key or network issues.\n")
        
        print("=" * 60)

def main():
    """Main function to test the simple AI agent"""
    
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key:")
        print("OPENAI_API_KEY=your_api_key_here")
        print("\nYou can get an API key from: https://platform.openai.com/api-keys")
        return
    
    # Create the agent
    agent = create_simple_agent()
    
    # Test questions covering different AI topics
    test_questions = [
        "What is generative AI and how does it differ from traditional AI?",
        "Explain the difference between supervised and unsupervised learning with examples",
        "What are the main challenges in deploying AI models to production?",
        "How do transformers work in natural language processing?",
        "What is the role of attention mechanisms in modern AI?"
    ]
    
    # Run the test
    test_agent(agent, test_questions)
    
    print("✅ Simple agent test completed!")

if __name__ == "__main__":
    main() 