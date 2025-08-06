import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

class CodeReviewAgent:
    """ Specialized agent for code review"""

    def __init__(self):
        self.llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature = 0.6)
        self.prompt_template = PromptTemplate(
                input_variables = ["code", "language"],
                template="""
                You are an expert code reviewer. Review the following {language} code:
                
                Code:
                {code}

                Please provide:
                1. Code quality assessment
                2. Potential issues or bugs
                3. Suggestions for improvement
                4. Security considerations (if applicable)

                Review:
                """)
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    def review_code(self, code, language=["Python", "C"]):
        """Review the provided code"""

        try:
            response = self.chain.run(code=code, language=language)
            return response
        except Exception as e:
            return f"Error during code review: {e}"

def main():
    """ Test the specialized code review agent"""

    # Create the agent
    agent = CodeReviewAgent()

    # Sample code to review
    sample_code = """
    def isFibonacci(n):
        if n <= 1:
            return n
        return isFibonacci(n-1) + isFibonacci(n-2)

    # Test the function
    result = isFibonacci(30)
    print(result)
    """
    print("🔍 Code Review Agent Test\n")
    print("Sample Code:")
    print(sample_code)
    print("-" * 83)

    # Get review
    review = agent.review_code(sample_code, "python")
    print("Code Review: ")
    print(review)

if __name__ == "__main__":
    main()
