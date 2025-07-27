# Student Guide - Assignment Submissions

Welcome to the Generative AI & Automation course! This guide will help you submit your assignments correctly and learn professional development practices.

## 🎯 Learning Objectives

This course teaches you:
- **Modern Software Development**: Git, CI/CD, and collaboration
- **Code Quality**: Testing, linting, and best practices
- **Security**: Secure coding and vulnerability prevention
- **Professional Workflow**: Real-world development practices

## 🚀 Quick Start

### Why Use a Submission Branch?
The submission branch workflow ensures that:
- **Main branch stays clean**: Always serves as a clean starter template
- **New students get fresh start**: Each new student gets the original course structure
- **Organized submissions**: All student work goes to a separate `student-submissions` branch
- **Easy maintenance**: Instructors can manage submissions without affecting the starter template
- **Proper separation**: Student work never pollutes the main branch

### 1. Fork the Repository
1. Go to the main course repository on GitHub
2. Click the "Fork" button in the top right
3. This creates your own copy of the repository

### 2. Clone Your Fork
```bash
# Replace 'your-username' with your actual GitHub username
git clone https://github.com/your-username/generative-ai-course.git
cd generative-ai-course
```

### 3. Create and Switch to Submission Branch
```bash
# Create and switch to a submission branch for your work
git checkout -b submission

# This keeps the main branch clean as a starter template
```

### 4. Set Up Your Environment
```bash
# Create a Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install course dependencies
pip install -r requirements.txt
```

## 📁 Assignment Structure

### Your Submission Folder
Create your work in the `student-submissions/` folder:

```
student-submissions/
└── your-username/
    ├── week-01/
    │   ├── README.md
    │   ├── assignment.py
    │   ├── requirements.txt
    │   └── data/
    ├── week-02/
    │   ├── README.md
    │   ├── project.py
    │   └── results/
    └── ...
```

### Required Files for Each Week
- **README.md**: Project description and instructions
- **Your code files**: Python scripts, notebooks, etc.
- **requirements.txt**: List of Python packages used
- **Any data files**: CSV, JSON, images, etc.

## 📝 Working on Assignments

### Step 1: Create Your Week Folder
```bash
# Create your week folder
mkdir -p student-submissions/your-username/week-01
cd student-submissions/your-username/week-01
```

### Step 2: Work on Your Assignment
- Write your code in Python files
- Create a comprehensive README.md
- Test your code thoroughly
- Document your approach and challenges

### Step 3: Commit Your Work
```bash
# Add your work
git add student-submissions/your-username/week-01/

# Commit with a descriptive message
git commit -m "Week 1: Implemented sentiment analysis using NLTK"

# Push to your submission branch
git push origin submission
```

## 🔄 Submitting Your Assignment

### Important: Branch Structure
The course repository uses this branch structure:
- **`main`**: Clean starter template (never contains student work)
- **`student-submissions`**: Branch where all student submissions are collected
- **`submission`**: Your personal branch for your work

### Step 1: Create a Pull Request
1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. **Important**: Set the base branch to `submission` and the compare branch to `submission`
4. Set the target to the original course repository's `student-submissions` branch (not main)
5. Use this title format: "Student Submission: Week X - [Your discord Name]"

### Step 2: Fill Out the PR Template
The template will automatically appear. Fill it out completely:

```markdown
## Student Information
- **Name**: [Your Full Name]
- **Week**: [Week Number]
- **Assignment**: [Assignment Title]
- **GitHub Username**: [Your GitHub Username]

## Description
Brief description of what you implemented and learned

## Files Added/Modified
- `student-submissions/your-username/week-X/README.md`
- `student-submissions/your-username/week-X/assignment.py`
- etc.

## Learning Outcomes
- What did you learn from this assignment?
- What challenges did you face?
- How did you overcome them?

## External Resources Used
- List any tutorials, documentation, or resources you used
- Include links where applicable

## Testing
- [ ] Code runs without errors
- [ ] All requirements are met
- [ ] Documentation is complete
- [ ] Code follows style guidelines
```

## 📋 Assignment Checklist

### Before Submitting
- [ ] Code is functional and well-documented
- [ ] README.md includes:
  - Project description
  - Setup instructions
  - Usage examples
  - Learning outcomes
- [ ] requirements.txt lists all dependencies
- [ ] Code follows Python style guidelines
- [ ] No sensitive information (API keys, passwords)
- [ ] All files are in the correct folder structure

### Code Quality Standards
- **Readable code**: Use clear variable names and comments
- **Documentation**: Include docstrings for functions
- **Error handling**: Handle potential errors gracefully
- **Testing**: Test your code with different inputs

## 🎯 Example Submission

### Week 1: Introduction to Python and AI

**File Structure:**
```
student-submissions/john-doe/week-01/
├── README.md
├── hello_ai.py
├── requirements.txt
└── data/
    └── sample_text.txt
```

**README.md Example:**
```markdown
# Week 1: Introduction to Python and AI

## Description
This assignment introduces basic Python concepts and simple AI text processing.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the program: `python hello_ai.py`

## Features
- Text preprocessing
- Simple sentiment analysis
- File I/O operations

## Learning Outcomes
- Learned Python basics
- Understood text processing
- Gained confidence with AI concepts

## Challenges
- Understanding list comprehensions
- Debugging file path issues

## Usage
```python
python hello_ai.py --input data/sample_text.txt
```

## Dependencies
- nltk==3.8.1
- pandas==1.5.3
```

## ❌ Common Mistakes to Avoid

### Don't Do This
- Submit work outside the `student-submissions/` folder
- Work directly on the main branch (use submission branch instead)
- Forget to include README.md
- Submit incomplete or non-functional code
- Include API keys or sensitive data
- Use unclear commit messages

### ✅ Do This Instead
- Put all work in `student-submissions/your-username/week-X/`
- Work on your submission branch (keeps main clean as starter template)
- Include comprehensive documentation
- Test your code before submitting
- Use environment variables for sensitive data
- Write descriptive commit messages

## 🔧 Development Tools

### Code Quality Tools
```bash
# Format your code
black student-submissions/your-username/week-X/

# Check for style issues
flake8 student-submissions/your-username/week-X/

# Run type checking
mypy student-submissions/your-username/week-X/

# Security check
bandit -r student-submissions/your-username/week-X/
```

### Testing Your Code
```bash
# Run your code
python student-submissions/your-username/week-X/assignment.py

# Test with different inputs
python -c "import sys; sys.path.append('.'); from student_submissions.your_username.week_X import assignment; print('Tests passed!')"
```

## 📞 Getting Help

### When You're Stuck
1. **Check the course materials** first
2. **Search existing issues** on GitHub
3. **Ask in the course forum** or chat
4. **Create a GitHub issue** for technical problems

### Support Resources
- **Course Documentation**: Check the main README and week folders
- **Python Documentation**: https://docs.python.org/
- **GitHub Help**: https://help.github.com/
- **Office Hours**: Schedule with instructors

## ⏰ Submission Deadlines

- **Weekly assignments**: Due by Sunday 11:59 PM
- **Late submissions**: May be accepted with penalty
- **Extensions**: Request at least 24 hours in advance

## 🔍 After Submission

### What Happens Next
1. **Automated checks**: CI/CD pipeline validates your submission
2. **Review process**: Instructors review your work
3. **Feedback**: You'll receive comments on your PR
4. **Merging**: If approved, your work gets merged into the `student-submissions` branch (not main)
5. **Grading**: Final grades posted within 1 week

### Branch Protection
- The `main` branch is protected and never receives student submissions
- All student work goes to the `student-submissions` branch
- This ensures new students always get a clean starter template

### Receiving Feedback
- Check your PR for comments
- Address any issues raised
- Update your code if needed
- Resubmit if required

## 📊 Grading Criteria

- **Functionality (40%)**: Does your code work as intended?
- **Code Quality (25%)**: Is your code clean and readable?
- **Documentation (20%)**: Is your project well-documented?
- **Creativity (15%)**: Does your work show understanding and innovation?

## 🎓 Career Development

### Building Your Portfolio
- Each assignment becomes a portfolio piece
- GitHub profile shows your work
- Employers can see your development process
- Demonstrates real-world skills

### Skills You're Learning
- **Git & GitHub**: Version control and collaboration
- **CI/CD**: Automated testing and deployment
- **Code Review**: Giving and receiving feedback
- **Documentation**: Writing clear, professional docs
- **Security**: Secure coding practices

## 🚀 Next Steps

### After Course Completion
- **Contribute to open source**: Use your new skills
- **Apply for internships**: Show your GitHub profile
- **Build personal projects**: Continue learning
- **Network**: Connect with other developers

### Becoming a Contributor
- Help other students
- Suggest improvements to the course
- Contribute to course materials
- Join the development team

## 📚 Additional Resources

### Learning Materials
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Git Best Practices](https://git-scm.com/book/en/v2)
- [Markdown Guide](https://www.markdownguide.org/)
- [LangChain Documentation](https://python.langchain.com/)

### Tools to Explore
- **VS Code**: Excellent Python development environment
- **Jupyter Notebooks**: Interactive development
- **GitHub Desktop**: Visual Git interface
- **Docker**: Containerization (advanced)

---

**Remember**: This is a learning experience! Don't be afraid to make mistakes, ask questions, and experiment. Your instructors are here to help you succeed and grow into a professional developer.


