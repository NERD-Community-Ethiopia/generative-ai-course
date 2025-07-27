# Week 1 Workshop: Environment Setup & First AI Agent

## 🎯 Workshop Objectives

By the end of this workshop, you will:
- Set up your complete development environment
- Learn the Git workflow for this course
- Create your first AI agent using LangChain
- Understand the submission process

## 🛠️ Prerequisites

Before starting this workshop, ensure you have:
- Python 3.8+ installed
- Git installed and configured
- A GitHub account
- A code editor (VS Code recommended)
- Docker (optional, for later weeks)

## 📋 Workshop Agenda

### Part 1: Environment Setup (30 minutes)
### Part 2: Git Workflow (30 minutes)
### Part 3: First AI Agent (60 minutes)
### Part 4: Submission Process (30 minutes)

---

## 🚀 Part 1: Environment Setup

### Step 1: Clone the Repository

```bash
# Fork the repository on GitHub first, then clone your fork
git clone https://github.com/<your-username>/generative-ai-course.git
cd generative-ai-course
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install required packages
pip install langchain openai python-dotenv requests
pip install jupyter notebook  # For interactive development
```

### Step 4: Environment Variables

Create a `.env` file in the root directory:

```bash
# .env
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

**Note**: You'll need to get API keys from:
- [OpenAI](https://platform.openai.com/api-keys)
- [Hugging Face](https://huggingface.co/settings/tokens)

---

## 🔄 Part 2: Git Workflow

### Step 1: Configure Git

```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 2: Create a Feature Branch

```bash
# Create and switch to a new branch
git checkout -b week-01-setup

# Verify you're on the new branch
git branch
```

### Step 3: Basic Git Commands

```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Week 1: Environment setup and first AI agent"

# Push to your fork
git push origin week-01-setup
```

---

## 🤖 Part 3: First AI Agent

### Exercise 1: Simple Chat Agent

Create a file `workshops/week-01/simple_agent.py`:

```python
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

def create_simple_agent():
    """Create a simple AI agent using OpenAI"""
    
    # Initialize the language model
    llm = OpenAI(temperature=0.7)
    
    # Create a prompt template
    template = """
    You are a helpful AI assistant. Answer the following question:
    
    Question: {question}
    
    Answer:"""
    
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )
    
    # Create the chain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    return chain

def main():
    """Main function to test the agent"""
    
    # Create the agent
    agent = create_simple_agent()
    
    # Test questions
    test_questions = [
        "What is generative AI?",
        "Explain the difference between supervised and unsupervised learning",
        "What are the main challenges in AI deployment?"
    ]
    
    print("🤖 Simple AI Agent Test\n")
    
    for i, question in enumerate(test_questions, 1):
        print(f"Question {i}: {question}")
        try:
            response = agent.run(question)
            print(f"Answer: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
        
        print("-" * 50)

if __name__ == "__main__":
    main()
```

### Exercise 2: Interactive Chat Agent

Create a file `workshops/week-01/interactive_agent.py`:

```python
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()

def create_interactive_agent():
    """Create an interactive AI agent with memory"""
    
    # Initialize the language model
    llm = OpenAI(temperature=0.7)
    
    # Create memory for conversation
    memory = ConversationBufferMemory()
    
    # Create conversation chain
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    return conversation

def chat_interface():
    """Interactive chat interface"""
    
    print("🤖 Interactive AI Agent")
    print("Type 'quit' to exit\n")
    
    # Create the agent
    agent = create_interactive_agent()
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for quit command
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye! 👋")
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        try:
            # Get response from agent
            response = agent.predict(input=user_input)
            print(f"AI: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    chat_interface()
```

### Exercise 3: Specialized Agent

Create a file `workshops/week-01/specialized_agent.py`:

```python
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

class CodeReviewAgent:
    """Specialized agent for code review"""
    
    def __init__(self):
        self.llm = OpenAI(temperature=0.3)
        
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
            response = self.chain.run(code=code, language=language)
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
```

---

## 📤 Part 4: Submission Process

### Step 1: Create Submission Directory

```bash
# Create your submission directory
mkdir -p student-submissions/<your-username>/week-01
```

### Step 2: Copy Your Work

```bash
# Copy your workshop files
cp workshops/week-01/*.py student-submissions/<your-username>/week-01/
```

### Step 3: Create Documentation

Create `student-submissions/<your-username>/week-01/README.md`:

```markdown
# Week 1 Submission - [Your Name]

## Environment Setup
- [x] Python 3.8+ installed
- [x] Virtual environment created
- [x] Dependencies installed
- [x] API keys configured

## Completed Exercises
- [x] Simple AI Agent
- [x] Interactive Chat Agent
- [x] Specialized Code Review Agent

## Challenges Faced
[Describe any challenges you encountered and how you solved them]

## Learning Outcomes
[What did you learn from this workshop?]

## Next Steps
[What would you like to explore next?]
```

### Step 4: Submit via Pull Request

```bash
# Add all changes
git add .

# Commit changes
git commit -m "Week 1: Complete workshop exercises and documentation"

# Push to your branch
git push origin week-01-setup
```

Then go to GitHub and create a pull request from your `week-01-setup` branch to the main repository.

---

## 🎯 Workshop Checklist

- [ ] Environment setup completed
- [ ] Git workflow understood
- [ ] Simple agent created and tested
- [ ] Interactive agent working
- [ ] Specialized agent implemented
- [ ] Documentation written
- [ ] Pull request submitted

## 🚀 Bonus Challenges

1. **Add Error Handling**: Improve the agents with better error handling
2. **Custom Prompts**: Create your own specialized agent for a domain you're interested in
3. **Memory Enhancement**: Add more sophisticated memory to the interactive agent
4. **API Integration**: Integrate with additional APIs (weather, news, etc.)

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Git Best Practices](https://git-scm.com/book/en/v2)

---

**Remember**: The goal is to learn by doing. Don't worry if everything doesn't work perfectly on the first try! 