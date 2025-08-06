import os
from dotenv import load_dotenv
from langchain_openai import OpenAI  
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

def create_simple_agent():
    """Create a simple AI agent using OpenAI"""
    
    # Initialize the language model with the API key
    api_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(api_key=api_key, temperature=0.7)  # Ensure API key is used here
    
    # Create a prompt template
    template = """
    You are a helpful AI assistant. Answer the following question:
    
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
            response = agent.invoke({"question": question})  
            print(f"Answer: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
        
        print("-" * 50)

if __name__ == "__main__":
    main()