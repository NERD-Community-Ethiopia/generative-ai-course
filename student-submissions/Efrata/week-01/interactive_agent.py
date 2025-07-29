import os
import requests
from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()

def get_weather(city):
    """Example API integration: fetch weather info from OpenWeatherMap"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Weather API key is not configured."

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return f"Weather info not found for {city}."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    except Exception as e:
        return f"Failed to fetch weather data: {e}"

def create_interactive_agent():
    """Create an interactive AI agent with enhanced memory and custom prompts"""

    # Custom system prompt
    template = """
    You are a friendly and helpful assistant.
    If the user asks about weather, use this format: 'weather in [city]'.
    
    Previous conversation:
    {history}

    User: {input}
    AI:"""

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=template
    )

    # Initialize the language model
    llm = OpenAI(temperature=0.7)

    # Use buffer memory
    memory = ConversationBufferMemory(return_messages=True)

    # Conversation chain
    conversation = ConversationChain(
        prompt=prompt,
        llm=llm,
        memory=memory,
        verbose=True
    )

    return conversation

def chat_interface():
    """Interactive chat interface with API integration"""

    print("🤖 Enhanced Interactive AI Agent")
    print("Type 'quit' to exit\n")

    agent = create_interactive_agent()

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye! 👋")
                break

            if not user_input:
                continue

            # Weather API hook
            if user_input.lower().startswith("weather in "):
                city = user_input[11:].strip()
                weather_info = get_weather(city)
                print(f"AI: {weather_info}\n")
                continue

            # AI response
            response = agent.predict(input=user_input)
            print(f"AI: {response}\n")

        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    chat_interface()
