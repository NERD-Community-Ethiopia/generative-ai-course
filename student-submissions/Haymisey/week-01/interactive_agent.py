"""
Interactive Chat Agent with Memory

This module creates an interactive AI agent that can maintain conversation context
using LangChain's memory capabilities. It demonstrates how to build a chat interface
that remembers previous interactions.
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()

def create_interactive_agent():
    """
    Create an interactive AI agent with memory
    
    Returns:
        ConversationChain: A conversation chain with memory capabilities
    """
    
    # Initialize the language model with moderate creativity
    llm = OpenAI(temperature=0.7)
    
    # Create memory for conversation context
    memory = ConversationBufferMemory()
    
    # Create conversation chain with memory
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True  # Set to False for cleaner output
    )
    
    return conversation

def chat_interface():
    """Interactive chat interface for the AI agent"""
    
    print("🤖 Interactive AI Agent with Memory")
    print("=" * 50)
    print("Type 'quit', 'exit', or 'bye' to end the conversation")
    print("Type 'clear' to clear the conversation memory")
    print("Type 'help' to see available commands")
    print("=" * 50)
    print()
    
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key:")
        print("OPENAI_API_KEY=your_api_key_here")
        print("\nYou can get an API key from: https://platform.openai.com/api-keys")
        return
    
    # Create the agent
    agent = create_interactive_agent()
    
    # Conversation counter
    message_count = 0
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for quit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("AI: Goodbye! It was great chatting with you! 👋")
                break
            
            # Check for clear command
            if user_input.lower() == 'clear':
                agent.memory.clear()
                print("AI: Conversation memory cleared! Starting fresh.")
                message_count = 0
                continue
            
            # Check for help command
            if user_input.lower() == 'help':
                print("AI: Available commands:")
                print("- 'quit', 'exit', 'bye': End the conversation")
                print("- 'clear': Clear conversation memory")
                print("- 'help': Show this help message")
                print("- Any other text: Chat with me!")
                continue
            
            # Skip empty input
            if not user_input:
                continue
            
            # Increment message counter
            message_count += 1
            
            # Get response from agent
            response = agent.predict(input=user_input)
            print(f"AI: {response}\n")
            
            # Show conversation stats every 5 messages
            if message_count % 5 == 0:
                print(f"💬 Conversation length: {message_count} messages")
                print("-" * 30)
            
        except KeyboardInterrupt:
            print("\n\nAI: Goodbye! Thanks for chatting! 👋")
            break
        except Exception as e:
            print(f"AI: Sorry, I encountered an error: {e}")
            print("Please try again or type 'quit' to exit.\n")

def demo_conversation():
    """Demonstrate the agent with a sample conversation"""
    
    print("🎭 Demo Conversation")
    print("=" * 30)
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  API key not found. Cannot run demo.")
        return
    
    agent = create_interactive_agent()
    
    # Sample conversation
    demo_messages = [
        "Hello! I'm learning about AI agents.",
        "Can you explain what LangChain is?",
        "How does memory work in conversation agents?",
        "What are the benefits of using memory in AI conversations?"
    ]
    
    for message in demo_messages:
        print(f"You: {message}")
        try:
            response = agent.predict(input=message)
            print(f"AI: {response}\n")
        except Exception as e:
            print(f"AI: Error - {e}\n")
    
    print("Demo completed!")

def main():
    """Main function to run the interactive agent"""
    
    print("Choose an option:")
    print("1. Start interactive chat")
    print("2. Run demo conversation")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            chat_interface()
            break
        elif choice == "2":
            demo_conversation()
            break
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main() 