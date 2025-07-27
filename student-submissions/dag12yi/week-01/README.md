# Week 1 Submission - dag12yi

## Project Description
This project contains my solutions for Week 1 of the Generative AI Course. The focus is on building simple, interactive, and specialized AI agents using the LangChain framework. (Add any special notes if you used a different API or model.)

## Environment Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd generative-ai-course/student-submissions/dag12yi/week-01
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**
   Create a `.env` file in this directory with:
   ```
   OPENAI_API_KEY=****_openai_api_key_****
   # or
   OPENROUTER_API_KEY=****_openrouter_key_****
   ```

## Usage Examples

**Simple AI Agent**
```bash
python simple_agent.py
```
_Example output:_
```
🤖 Simple AI Agent Test

Question 1: What is generative AI?
Answer: ...
--------------------------------------------------
```

**Interactive Chat Agent**
```bash
python interactive_agent.py
```
_Example output:_
```
🤖 Interactive AI Agent
Type 'quit' to exit

You: Hello
AI: Hello! ...
```

**Specialized Code Review Agent**
```bash
python specialized_agent.py
```
_Example output:_
```
🔍 Code Review Agent Test

Sample Code:
...
--------------------------------------------------
Code Review:
1. Code quality assessment: ...
2. Potential issues or bugs: ...
3. Suggestions for improvement: ...
4. Security considerations (if applicable): ...
```

## Completed Exercises
- [x] Simple AI Agent
- [x] Interactive Chat Agent
- [x] Specialized Code Review Agent

## Challenges Faced
During this workshop, I encountered several challenges:
- **Requirements Installation:** The provided requirements.txt included several Linux/Ubuntu-specific packages (such as `command-not-found`, `distro-info`, `python-apt`, etc.) that are not available on Windows or via PyPI. This caused repeated installation errors and required manual editing of the requirements file to comment out or remove problematic packages.
- **Virtual Environment (venv):** I initially did not understand the purpose and use of Python virtual environments (`venv`). After some research, I learned that `venv` helps isolate project dependencies, preventing conflicts between packages required by different projects. Activating the virtual environment ensures that all installed packages are local to the project and do not affect the global Python installation.

## Learning Outcomes
- Gained hands-on experience with the LangChain framework by implementing three types of AI agents: [simple_agent.py](simple_agent.py), [interactive_agent.py](interactive_agent.py), and [specialized_agent.py](specialized_agent.py).
- Learned how to set up and activate a Python virtual environment (`venv`) to manage dependencies in isolation.
- Understood the importance of carefully managing and editing requirements files, especially when working across different operating systems.
- Practiced using environment variables and `.env` files to securely manage API keys for services like OpenAI.
- Improved my ability to troubleshoot installation and compatibility issues in Python projects.

## Next Steps
- Explore more advanced features of LangChain, such as integrating external tools, custom memory modules, or chaining multiple agents together.
- Experiment with different language models and providers (e.g., OpenRouter, Hugging Face) by updating the agent scripts to use alternative APIs.
- Refactor and document the agent scripts further to make them more robust and user-friendly.
- Share my solutions and experiences with peers, and review their submissions for additional learning.
- Continue building on these foundational agents in future weeks, applying lessons learned from [simple_agent.py](simple_agent.py), [interactive_agent.py](interactive_agent.py), and [specialized_agent.py](specialized_agent.py). 