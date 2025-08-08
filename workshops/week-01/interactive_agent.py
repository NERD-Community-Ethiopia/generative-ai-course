import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Modern import
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory


# Load environment variables
load_dotenv()

def create_interactive_agent():
    """Create an interactive AI agent with memory (modern syntax)"""
    # Initialize the language model
    llm = ChatOpenAI(temperature=0.7)  # Updated to ChatOpenAI
    
    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Be conversational and provide detailed answers."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    # Create the chain
    chain = prompt | llm
    
    # Add conversation memory
    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: ChatMessageHistory(),  # Memory storage
        input_messages_key="input",
        history_messages_key="history"
    )
    
    return chain_with_history

def chat_interface():
    """Interactive chat interface"""   
    print("🤖 Interactive AI Agent")
    print("Type 'quit' to exit\n")
    
    # Create the agent
    agent = create_interactive_agent()
    session_id = "user_session_1"  # Can be dynamic per user
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye! 👋")
                break
                
            if not user_input:
                continue
                
            # Get response
            response = agent.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            )
            print(f"AI: {response.content}\n")  # ChatOpenAI returns .content
            
        except Exception as e:
            print(f"Error: {str(e)[:200]}\n")  # Truncate long errors
 
if __name__ == "__main__":
    chat_interface()