import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import requests

# Load environment variables
load_dotenv()


class CodeReviewAgent:
    """Security-focused code review agent with memory and CVE suggestion"""

    def __init__(self, temperature=0.3):
        # Initialize the LLM with memory
        self.llm = OpenAI(temperature=temperature)
        self.memory = ConversationBufferMemory(memory_key="chat_history")

        # Custom prompt template focused on secure code practices
        self.prompt_template = PromptTemplate(
            input_variables=["code", "language", "chat_history"],
            template="""
You are a senior cybersecurity expert and code reviewer. Review the following {language} code for potential issues.

{chat_history}

Code:
{code}

Please respond with:
1. Code Quality Assessment
2. Bugs or Logical Issues
3. Security Vulnerabilities (with references if possible)
4. Suggestions for Improvement

Only include explanations relevant to the code's context.

Review:
"""
        )

        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt_template,
            memory=self.memory
        )

    def fetch_related_cve(self, keyword):
        """Mockup: Simulate CVE lookup via an API"""
        # Replace with a real CVE API like NVD or VulDB for production use
        mock_database = {
            "recursion": "CVE-2021-44228",
            "input validation": "CVE-2020-0601",
            "buffer overflow": "CVE-2017-5638"
        }
        for key, cve in mock_database.items():
            if key in keyword.lower():
                return f"Related vulnerability: {cve}"
        return "No known CVEs found related to this code."

    def review_code(self, code, language="Python"):
        """Review the provided code and fetch any related CVEs"""
        try:
            # Run the review agent
            response = self.chain.run(code=code, language=language)

            # Basic keyword search for related CVE
            cve_hint = self.fetch_related_cve(code)

            return f"{response}\n\n🔐 {cve_hint}"
        except Exception as e:
            return f"🚨 Error during code review: {str(e)}"


def main():
    """Run the enhanced code review agent"""

    # Create the agent
    agent = CodeReviewAgent()

    # Sample code to review (intentionally inefficient and recursive)
    sample_code = """
def calculate_fibonacci(n):
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

# Test the function
result = calculate_fibonacci(10)
print(result)
"""

    print("🔍 Secure Code Review Agent\n")
    print("Sample Code:")
    print(sample_code)
    print("-" * 50)

    # Run review
    review_result = agent.review_code(sample_code, "Python")
    print("Review Output:")
    print(review_result)


if __name__ == "__main__":
    main()
