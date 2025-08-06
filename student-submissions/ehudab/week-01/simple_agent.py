import os
from dotenv import load_dotenv
# Use ChatOpenAI from langchain_openai for OpenRouter
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables (expects OPENROUTER_API_KEY in .env)
load_dotenv()

def create_simple_agent():
    """Create a simple AI agent using OpenRouter's Qwen model via LangChain"""
    # Initialize the language model with OpenRouter endpoint and Qwen model
    llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",  # OpenRouter endpoint
        model="qwen/qwen3-coder:free",            # Qwen Coder (free) model
        temperature=0.7,
        api_key=os.getenv("OPENROUTER_API_KEY")    # API key from .env
    )
    
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
            # Use .invoke() instead of deprecated .run()
            response = agent.invoke({"question": question})
            print(f"Answer: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
        
        print("-" * 50)

if __name__ == "__main__":
    main()