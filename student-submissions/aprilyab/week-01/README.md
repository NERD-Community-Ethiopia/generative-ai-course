# Week 1 Submission - Henok Yoseph

##  Environment Setup
- [x] Installed Python 3.8+ and verified the version
- [x] Created and activated a virtual environment successfully
- [x] Installed all dependencies including LangChain, OpenAI, dotenv, and requests
- [x] Created a `.env` file and configured my OpenAI and Hugging Face API keys

##  Completed Exercises
- [x] `simple_agent.py` - A basic AI assistant that responds to static queries
- [x] `interactive_agent.py` - An interactive chatbot with memory buffer for context retention
- [x] `specialized_agent.py` - A focused AI agent that performs intelligent code reviews

##  Challenges Faced
One issue I faced was an error related to environment variables not being loaded properly. After checking my file paths and confirming the `.env` file location, I realized I hadn't called `load_dotenv()` at the top of each script. Once fixed, the agents began functioning correctly.

Another challenge was understanding how LangChain chains worked. Initially, I misunderstood how to link prompts and LLMs but reviewing the documentation and experimenting helped clarify the process.

##  Learning Outcomes
- Understood how to set up a full Python-based AI development environment
- Gained practical experience with the LangChain framework
- Learned to create prompt templates and link them to LLM chains
- Understood how to work with conversational memory
- Practiced writing a basic code review agent using natural language prompts

##  Next Steps
- Explore LangChain's advanced features such as Tools and Agents
- Build a domain-specific agent (e.g., an educational tutor or data analyst)
- Learn how to persist conversation history beyond runtime
- Experiment with integrating external APIs to enhance agent capabilities

