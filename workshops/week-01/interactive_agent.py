import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()

def create_interactive_agent():
    """Create an interactive AI agent with memory"""
    
    # Initialize the language model
    llm = OpenAI(temperature=0.7)
    
    # Create memory for conversation
    memory = ConversationBufferMemory()
    
    # Create conversation chain
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    return conversation

def chat_interface():
    """Interactive chat interface"""
    
    print("🤖 Interactive AI Agent")
    print("Type 'quit' to exit\n")
    
    # Create the agent
    agent = create_interactive_agent()
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for quit command
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye! 👋")
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        try:
            # Get response from agent
            response = agent.predict(input=user_input)
            print(f"AI: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    chat_interface()
