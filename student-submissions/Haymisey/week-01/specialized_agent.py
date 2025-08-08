"""
Specialized Code Review Agent

This module creates a specialized AI agent for code review using LangChain.
The agent can analyze code snippets and provide comprehensive feedback including
code quality assessment, potential issues, improvement suggestions, and security considerations.
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

class CodeReviewAgent:
    """
    Specialized agent for code review and analysis
    
    This agent can review code in various programming languages and provide
    detailed feedback on code quality, potential issues, and improvements.
    """
    
    def __init__(self, temperature=0.3):
        """
        Initialize the code review agent
        
        Args:
            temperature (float): Controls randomness in responses (0.0-1.0)
        """
        self.llm = OpenAI(temperature=temperature)
        
        # Create a comprehensive prompt template for code review
        self.prompt_template = PromptTemplate(
            input_variables=["code", "language"],
            template="""
            You are an expert code reviewer with deep knowledge of software engineering best practices.
            Please review the following {language} code and provide a comprehensive analysis:
            
            Code:
            {code}
            
            Please provide a detailed review covering:
            
            1. **Code Quality Assessment**:
               - Readability and maintainability
               - Code structure and organization
               - Naming conventions and clarity
            
            2. **Potential Issues or Bugs**:
               - Logic errors or edge cases
               - Performance concerns
               - Potential runtime errors
            
            3. **Suggestions for Improvement**:
               - Code optimization opportunities
               - Better practices to follow
               - Refactoring suggestions
            
            4. **Security Considerations** (if applicable):
               - Input validation
               - Data handling security
               - Authentication/authorization concerns
            
            5. **Overall Rating**: Rate the code from 1-10 and provide a brief summary
            
            Review:"""
        )
        
        # Create the chain
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
    
    def review_code(self, code, language="Python"):
        """
        Review the provided code
        
        Args:
            code (str): The code snippet to review
            language (str): Programming language of the code
            
        Returns:
            str: Detailed code review feedback
        """
        try:
            response = self.chain.run(code=code, language=language)
            return response
        except Exception as e:
            return f"Error during code review: {e}"
    
    def review_multiple_files(self, code_files):
        """
        Review multiple code files
        
        Args:
            code_files (list): List of tuples (code, language, filename)
            
        Returns:
            dict: Dictionary with filename as key and review as value
        """
        reviews = {}
        
        for code, language, filename in code_files:
            print(f"🔍 Reviewing {filename}...")
            review = self.review_code(code, language)
            reviews[filename] = review
            print(f"✅ Review completed for {filename}\n")
        
        return reviews

def get_sample_code_snippets():
    """Get sample code snippets for testing"""
    
    samples = [
        # Good Python code
        {
            "code": """
def calculate_fibonacci(n):
    \"\"\"Calculate the nth Fibonacci number using dynamic programming.\"\"\"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Use dynamic programming for efficiency
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib[n]

# Test the function
if __name__ == "__main__":
    result = calculate_fibonacci(10)
    print(f"Fibonacci(10) = {result}")
""",
            "language": "Python",
            "description": "Good Python code with proper documentation and efficient algorithm"
        },
        
        # Code with issues
        {
            "code": """
def calc_fib(n):
    if n <= 1:
        return n
    return calc_fib(n-1) + calc_fib(n-2)

result = calc_fib(10)
print(result)
""",
            "language": "Python",
            "description": "Inefficient recursive implementation without memoization"
        },
        
        # Security-sensitive code
        {
            "code": """
import os

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

# User input without validation
user_file = input("Enter file path: ")
content = read_file(user_file)
print(content)
""",
            "language": "Python",
            "description": "Code with potential security vulnerabilities"
        }
    ]
    
    return samples

def main():
    """Main function to test the specialized code review agent"""
    
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key:")
        print("OPENAI_API_KEY=your_api_key_here")
        print("\nYou can get an API key from: https://platform.openai.com/api-keys")
        return
    
    # Create the agent
    agent = CodeReviewAgent()
    
    print("🔍 Code Review Agent Test")
    print("=" * 50)
    
    # Get sample code snippets
    samples = get_sample_code_snippets()
    
    # Review each sample
    for i, sample in enumerate(samples, 1):
        print(f"\n📝 Sample {i}: {sample['description']}")
        print("-" * 50)
        print("Code:")
        print(sample['code'])
        print("-" * 50)
        
        # Get review
        review = agent.review_code(sample['code'], sample['language'])
        print("Code Review:")
        print(review)
        print("=" * 80)
    
    print("\n✅ Code review agent test completed!")

def interactive_review():
    """Interactive code review interface"""
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  API key not found. Cannot run interactive review.")
        return
    
    agent = CodeReviewAgent()
    
    print("🔍 Interactive Code Review")
    print("=" * 30)
    print("Enter your code (type 'END' on a new line to finish):")
    print()
    
    code_lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        code_lines.append(line)
    
    if code_lines:
        code = "\n".join(code_lines)
        language = input("Enter programming language (default: Python): ").strip() or "Python"
        
        print("\n🔍 Reviewing your code...")
        review = agent.review_code(code, language)
        print("\n📋 Code Review:")
        print(review)
    else:
        print("No code provided.")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Run sample code reviews")
    print("2. Interactive code review")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        main()
    elif choice == "2":
        interactive_review()
    elif choice == "3":
        print("Goodbye! 👋")
    else:
        print("Invalid choice. Running sample reviews...")
        main() 