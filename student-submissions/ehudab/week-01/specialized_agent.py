import os
from dotenv import load_dotenv
# Use ChatOpenAI from langchain_openai for OpenRouter
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables (expects OPENROUTER_API_KEY in .env)
load_dotenv()

class CodeReviewAgent:
    """Specialized agent for code review using OpenRouter's Qwen model"""
    
    def __init__(self):
        # Initialize the language model with OpenRouter endpoint and Qwen model
        self.llm = ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",  # OpenRouter endpoint
            model="qwen/qwen3-coder:free",            # Qwen Coder (free) model
            temperature=0.3,
            api_key=os.getenv("OPENROUTER_API_KEY")    # API key from .env
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["code", "language"],
            template="""
            You are an expert code reviewer. Review the following {language} code:
            
            Code:
            {code}
            
            Please provide:
            1. Code quality assessment
            2. Potential issues or bugs
            3. Suggestions for improvement
            4. Security considerations (if applicable)
            
            Review:"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
    
    def review_code(self, code, language="Python"):
        """Review the provided code"""
        try:
            # Use .invoke() instead of deprecated .run()
            response = self.chain.invoke({"code": code, "language": language})
            return response
        except Exception as e:
            return f"Error during code review: {e}"

def main():
    """Test the specialized code review agent"""
    
    # Create the agent
    agent = CodeReviewAgent()
    
    # Sample code to review
    sample_code = """
    def calculate_fibonacci(n):
        if n <= 1:
            return n
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    
    # Test the function
    result = calculate_fibonacci(10)
    print(result)
    """
    
    print("🔍 Code Review Agent Test\n")
    print("Sample Code:")
    print(sample_code)
    print("-" * 50)
    
    # Get review
    review = agent.review_code(sample_code, "Python")
    print("Code Review:")
    print(review)

if __name__ == "__main__":
    main()