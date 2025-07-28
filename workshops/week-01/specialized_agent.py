import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Modern import
from langchain_core.prompts import ChatPromptTemplate  # Updated prompt system
from langchain_core.runnables import RunnablePassthrough

# Load environment variables
load_dotenv()

class CodeReviewAgent:
    """Modern specialized code review agent"""
    
    def __init__(self):
        # Initialize modern ChatOpenAI
        self.llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")
        
        # Modern prompt template with structured output
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are an expert code reviewer. Analyze the provided code and return:
            1. Code quality assessment (bullet points)
            2. Potential issues/bugs (bullet points)
            3. Improvement suggestions (bullet points)
            4. Security considerations (if any)"""),
            ("human", "Language: {language}\nCode:\n{code}")
        ])
        
        # Modern chain construction
        self.chain = (
            {"code": RunnablePassthrough(), "language": RunnablePassthrough()}
            | self.prompt_template
            | self.llm
        )
    
    def review_code(self, code, language="Python"):
        """Review code using modern LangChain syntax"""
        try:
            response = self.chain.invoke({"code": code, "language": language})
            return response.content
        except Exception as e:
            return f"Error during code review: {str(e)[:200]}"

def main():
    """Test the modernized agent"""
    agent = CodeReviewAgent()
    
    sample_code = """
    def calculate_fibonacci(n):
        if n <= 1:
            return n
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    
    result = calculate_fibonacci(10)
    print(result)
    """
    
    print("🔍 Modern Code Review Agent\n")
    print("Sample Code:", sample_code, "-" * 50, sep="\n")
    
    review = agent.review_code(sample_code)
    print("Code Review:\n", review)

if __name__ == "__main__":
    main()