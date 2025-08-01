import os
from dotenv import load_dotenv
from datetime import datetime

# LangChain imports
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Simulate external API (could be replaced with real API)
def fetch_security_guidelines(language):
    guidelines = {
        "Python": "- Avoid using `eval()`\n- Sanitize user input\n- Use virtual environments\n- Validate dependencies",
        "JavaScript": "- Sanitize DOM inputs\n- Avoid `eval()`\n- Use HTTPS\n- Prevent XSS with proper escaping",
    }
    return guidelines.get(language, "No specific security guidelines found.")

# Load environment variables
load_dotenv()

class CodeReviewAgent:
    """Specialized code review agent with memory, API integration, and error handling."""
    
    def __init__(self):
        try:
            self.llm = OpenAI(temperature=0.3)

            # Add memory
            self.memory = ConversationBufferMemory()

            self.prompt_template = PromptTemplate(
                input_variables=["code", "language", "guidelines"],
                template="""
You are a senior code reviewer. Analyze the following {language} code:

{code}

Use the following security guidelines during the review:
{guidelines}

Please provide:
1. Code quality assessment
2. Potential bugs or issues
3. Suggestions for improvement
4. Security considerations

Be clear, concise, and professional.

Review:"""
            )

            self.chain = LLMChain(
                llm=self.llm, 
                prompt=self.prompt_template, 
                memory=self.memory,
                verbose=False
            )

        except Exception as e:
            raise RuntimeError(f"Failed to initialize the agent: {e}")
    
    def review_code(self, code, language="Python"):
        """Generate a code review with memory + simulated API data."""
        try:
            guidelines = fetch_security_guidelines(language)
            response = self.chain.run(code=code, language=language, guidelines=guidelines)

            # Save review to memory manually for tracking
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.memory.save_context({"input": f"{language} code review @ {timestamp}"}, {"output": response})

            return response
        except Exception as e:
            return f"⚠️ Error during code review: {e}"

    def show_memory(self):
        """Display stored memory (review history)."""
        return self.memory.buffer


def main():
    print("🔍 Code Review Agent – Enhanced Version\n")

    agent = CodeReviewAgent()

    sample_code = """
def calculate_fibonacci(n):
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

result = calculate_fibonacci(10)
print(result)
"""

    print("🧪 Sample Code:")
    print(sample_code)
    print("\n📋 Review:\n" + "-"*50)

    review = agent.review_code(sample_code, language="Python")
    print(review)

    print("\n🧠 Review History:")
    print(agent.show_memory())


if __name__ == "__main__":
    main()
