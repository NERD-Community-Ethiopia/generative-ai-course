import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Load environment variables
load_dotenv()

def create_simple_agent():
    """Create a simple AI agent using HuggingFace"""
    
    # Initialize the HuggingFace language model
    llm = HuggingFaceEndpoint(
        repo_id="google/flan-t5-large",
        temperature=0.7,
         # Changed to max_new_tokens
        task= "text2text-genetration"
    )
    
    # Create a prompt template
    template = """You are a helpful AI assistant. Answer the following question:
    
    Question: {question}
    
    Answer:"""
    
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )
    
    # Create the chain using the new recommended syntax
    chain = (
        {"question": RunnablePassthrough()} 
        | prompt 
        | llm
    )
    
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
    
    print("🤖 Simple AI Agent Test (HuggingFace)\n")
    
    for i, question in enumerate(test_questions, 1):
        print(f"Question {i}: {question}")
        try:
            response = agent.invoke(question)
            print(f"Answer: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
        
        print("-" * 50)

if __name__ == "__main__":
    main()