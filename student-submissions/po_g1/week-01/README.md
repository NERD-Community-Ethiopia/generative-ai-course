# Week 1 Submission - AI Agent with LangChain

## Student Information
- **Name**: Rediet Girmay  
- **Discord**: @po_g1  
- **GitHub**: [LuminaryDev](https://github.com/LuminaryDev) 

## Description
This submission demonstrates three foundational AI agents built using LangChain:
1. A **Q&A agent** answering technical AI questions
2. An **interactive chatbot** with conversation memory
3. A **code review specialist** analyzing Python implementations

## Environment Setup
- [x] Python 3.12.6 installed and verified
- [x] Virtual environment created and activated
- [x] Required packages installed (langchain, openai, python-dotenv)
- [x] API keys configured in `.env` file (OpenAI + HuggingFace)

## Completed Exercises
- [x] **Simple AI Agent**: Implemented Q&A functionality with predefined questions
- [x] **Interactive Agent**: Built conversational AI with memory persistence
- [x] **Specialized Agent**: Created code review tool with quality assessment features

## Challenges Faced
1. **API Limitations**  
   - Triggered OpenAI's rate limits during testing  
   - Solution: Implemented error handling + backup API keys 
   
2. **Deprecation Warnings**:
   - Updated from `langchain.llms` to `langchain_openai`
   - Modernized chain syntax using `RunnablePassthrough`

3. **Environment Issues**:
   - Fixed `.env` file loading problems
   - Verified absolute paths for reliability

## Learning Outcomes
- **Technical Skills**:
  - LangChain architecture fundamentals
  - Proper API key management
  - Git feature branching strategy

- **Problem Solving**:
  - Debugging quota-related HTTP errors
  - Resolving package version conflicts

## Next Steps
- [ ] Implement input validation for agents
- [ ] Add unit tests using pytest
- [ ] Containerize with Docker for portability
- [ ] Explore HuggingFace integration as OpenAI alternative

## Verification
All agents were tested locally with:
```bash
python simple_agent.py
python interactive_agent.py 
python specialized_agent.py

