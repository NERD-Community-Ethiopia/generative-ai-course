# Week 1 Submission - Ehud Ab

## Project Description
This project contains my solutions for Week 1 of the Generative AI Course. The focus is on building simple, interactive, and specialized AI agents using the LangChain framework. Due to the unavailability of the OpenAI API, all agents use the OpenRouter API with the free Qwen model (Qwen3 Coder). The project demonstrates how to set up a Python environment, manage API keys, and interact with large language models (LLMs) using LangChain.

## Environment Setup
Follow these steps to set up your environment:

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd generative-ai-course/student-submissions/ehudab/week-01
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure API keys**
   - Create a `.env` file in this directory with the following content:
     ```env
     OPENROUTER_API_KEY=sk-...your_openrouter_key...
     ```

## Usage Examples
Run any of the agent scripts from the command line:

- **Simple AI Agent**
  ```bash
  python simple_agent.py
  ```
  Example output:
  ```
  🤖 Simple AI Agent Test

  Question 1: What is generative AI?
  Answer: {'question': 'What is generative AI?', 'text': 'Generative AI is a type of artificial intelligence that can create new content by learning patterns from existing data. ...'}
  --------------------------------------------------
  Question 2: Explain the difference between supervised and unsupervised learning
  Answer: {'question': 'Explain the difference between supervised and unsupervised learning', 'text': 'Supervised and unsupervised learning are two fundamental approaches in machine learning ...'}
  --------------------------------------------------
  Question 3: What are the main challenges in AI deployment?
  Answer: {'question': 'What are the main challenges in AI deployment?', 'text': 'The main challenges in AI deployment include: ...'}
  --------------------------------------------------
  ```
  *Note: The output is a dictionary with both the question and the generated answer text.*

- **Interactive Chat Agent**
  ```bash
  python interactive_agent.py
  ```
  Example output:
  ```
  🤖 Interactive AI Agent
  Type 'quit' to exit

  You: Hello
  AI: Hello! It's nice to meet you. I'm an AI assistant, and I'm here to help with whatever questions or tasks you might have. Is there anything particular you'd like to chat about or any way I can assist you today?
  ```

- **Specialized Code Review Agent**
  ```bash
  python specialized_agent.py
  ```
  Example output:
  ```
  🔍 Code Review Agent Test

  Sample Code:
      def calculate_fibonacci(n):
          if n <= 1:
              return n
          return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

      # Test the function
      result = calculate_fibonacci(10)
      print(result)
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
- The OpenAI API was not available, so I used the OpenRouter API as an alternative.
- Integrated the free Qwen model (Qwen3 Coder) via OpenRouter instead of OpenAI models.
- Learned how to configure API keys and update code to use new LLM providers.

## Learning Outcomes
- How to set up and use Git for version control.
- How to use LangChain to build AI agents.
- How to manage API keys securely with environment variables.
- How to use OpenRouter as an alternative to OpenAI for LLMs.
- How to use Hugging Face and other model providers.

## Next Steps
- Explore how to train a language model from scratch or fine-tune an existing model.
- Learn about the process and requirements for creating a new AI model. 