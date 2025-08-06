import os
import requests
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetch_weather(city_name):
    """Fetch weather from OpenWeather API"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code != 200 or "weather" not in data:
            return "❌ Could not fetch weather data. Please check the city name."

        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return (
            f"🌤 Weather in {city_name}:\n"
            f"Description: {weather_desc}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
    except Exception as e:
        return f"Error fetching weather: {e}"

def is_weather_question(text):
    """Simple keyword-based check to detect weather questions"""
    keywords = ["weather", "temperature", "forecast"]
    return any(kw in text.lower() for kw in keywords)

def extract_city(text):
    """Extract city name using basic heuristic"""
    import re
    match = re.search(r"in ([A-Za-z\s]+)", text.lower())
    return match.group(1).strip().title() if match else None

def create_interactive_agent():
    """Create a conversational agent with memory"""
    llm = OpenAI(temperature=0.7)
    memory = ConversationBufferMemory()
    return ConversationChain(llm=llm, memory=memory, verbose=False)

def chat_interface():
    """Interactive CLI chat interface with weather support"""
    print("🤖 Interactive AI Agent")
    print("Ask me anything, including weather like: 'What's the weather in Nairobi?'\n(Type 'quit' to exit)\n")

    agent = create_interactive_agent()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye! 👋")
            break
        if not user_input:
            continue

        # Weather detection
        if is_weather_question(user_input):
            city = extract_city(user_input)
            if city:
                response = fetch_weather(city)
            else:
                response = "Please specify a city like: 'What's the weather in Paris?'"
        else:
            try:
                response = agent.predict(input=user_input)
            except Exception as e:
                response = f"⚠️ Error: {e}"

        print(f"AI: {response}\n")

if __name__ == "__main__":
    chat_interface()
