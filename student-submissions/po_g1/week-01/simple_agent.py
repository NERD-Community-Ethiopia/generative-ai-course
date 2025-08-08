import os
from dotenv import load_dotenv
from langchain_openai import OpenAI  # Modern import
from langchain_core.prompts import PromptTemplate  # Updated import
from langchain_core.runnables import RunnablePassthrough  # New for modern chains

# Load environment variables
load_dotenv()

def create_simple_agent():
    """Create a simple AI agent using OpenAI (modern syntax)"""
    # Initialize the language model
    llm = OpenAI(temperature=0.7)
    
    # Create a prompt template (modern style)
    prompt = PromptTemplate.from_template("""
    You are a helpful AI assistant. Answer the following question:
    
    Question: {question}
    
    Answer:""")
    
    # Modern chain construction
    chain = (
        {"question": RunnablePassthrough()} 
        | prompt 
        | llm
    )
    return chain

def main():
    """Main function to test the agent"""
    agent = create_simple_agent()
    test_questions = [
        "What is generative AI?",
        "Explain supervised vs unsupervised learning",
        "What are AI deployment challenges?"
    ]
    
    print("🤖 Simple AI Agent Test (Modern)\n")
    for i, question in enumerate(test_questions, 1):
        print(f"Question {i}: {question}")
        try:
            # Modern invocation
            response = agent.invoke(question)
            print(f"Answer: {response}\n")
        except Exception as e:
            print(f"Error: {str(e)[:200]}\n")  # Truncate long errors
        print("-" * 50)

if __name__ == "__main__":
    main()