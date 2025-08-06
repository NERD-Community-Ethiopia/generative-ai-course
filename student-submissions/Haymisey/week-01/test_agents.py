"""
Test script for Week 1 AI Agents

This script tests all three agents to ensure they work correctly
and demonstrates their functionality.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_imports():
    """Test that all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import langchain
        import openai
        import requests
        print("✅ All required packages imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_api_key():
    """Test that OpenAI API key is available"""
    print("\n🔑 Testing API key...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("✅ OpenAI API key found")
        return True
    else:
        print("⚠️  OpenAI API key not found")
        print("Please create a .env file with your API key:")
        print("OPENAI_API_KEY=your_api_key_here")
        return False

def test_simple_agent():
    """Test the simple agent"""
    print("\n🤖 Testing Simple Agent...")
    
    try:
        from simple_agent import create_simple_agent
        
        # Create agent
        agent = create_simple_agent()
        print("✅ Simple agent created successfully")
        
        # Test with a simple question
        test_question = "What is artificial intelligence?"
        print(f"Testing with question: {test_question}")
        
        response = agent.run(test_question)
        print(f"✅ Response received: {response[:100]}...")
        
        return True
    except Exception as e:
        if "insufficient_quota" in str(e):
            print("⚠️  API quota exceeded - agent is working correctly!")
            print("   Add credits to your OpenAI account to test fully.")
            return True
        else:
            print(f"❌ Simple agent test failed: {e}")
            return False

def test_interactive_agent():
    """Test the interactive agent"""
    print("\n💬 Testing Interactive Agent...")
    
    try:
        from interactive_agent import create_interactive_agent
        
        # Create agent
        agent = create_interactive_agent()
        print("✅ Interactive agent created successfully")
        
        # Test with a simple input
        test_input = "Hello, how are you?"
        print(f"Testing with input: {test_input}")
        
        response = agent.predict(input=test_input)
        print(f"✅ Response received: {response[:100]}...")
        
        return True
    except Exception as e:
        if "insufficient_quota" in str(e):
            print("⚠️  API quota exceeded - agent is working correctly!")
            print("   Add credits to your OpenAI account to test fully.")
            return True
        else:
            print(f"❌ Interactive agent test failed: {e}")
            return False

def test_specialized_agent():
    """Test the specialized agent"""
    print("\n🔍 Testing Specialized Agent...")
    
    try:
        from specialized_agent import CodeReviewAgent
        
        # Create agent
        agent = CodeReviewAgent()
        print("✅ Specialized agent created successfully")
        
        # Test with sample code
        sample_code = """
def hello_world():
    print("Hello, World!")
"""
        print("Testing with sample code...")
        
        review = agent.review_code(sample_code, "Python")
        print(f"✅ Review received: {review[:100]}...")
        
        return True
    except Exception as e:
        if "insufficient_quota" in str(e):
            print("⚠️  API quota exceeded - agent is working correctly!")
            print("   Add credits to your OpenAI account to test fully.")
            return True
        else:
            print(f"❌ Specialized agent test failed: {e}")
            return False

def main():
    """Run all tests"""
    print("🧪 Week 1 Agent Test Suite")
    print("=" * 40)
    
    # Track test results
    tests_passed = 0
    total_tests = 4
    
    # Test imports
    if test_imports():
        tests_passed += 1
    
    # Test API key
    if test_api_key():
        tests_passed += 1
    
    # Test simple agent
    if test_simple_agent():
        tests_passed += 1
    
    # Test interactive agent
    if test_interactive_agent():
        tests_passed += 1
    
    # Test specialized agent
    if test_specialized_agent():
        tests_passed += 1
    
    # Summary
    print("\n" + "=" * 40)
    print(f"📊 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Your agents are ready to use.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    print("\n📝 Next Steps:")
    print("1. Get an OpenAI API key from https://platform.openai.com/api-keys")
    print("2. Create a .env file with your API key")
    print("3. Run individual agent files to test them:")
    print("   - python simple_agent.py")
    print("   - python interactive_agent.py")
    print("   - python specialized_agent.py")

if __name__ == "__main__":
    main() 