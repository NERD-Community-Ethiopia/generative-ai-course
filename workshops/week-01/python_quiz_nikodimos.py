"""
Python Basics Quiz
"""

def run_quiz():
    score = 0
    questions = [
        {
            "question": "What is the output of 'print(3 * '7')'?",
            "options": ["A. 21", "B. 777", "C. '21'", "D. Error"],
            "answer": "B"
        },
        {
            "question": "Which of these is NOT a Python data type?",
            "options": ["A. list", "B. tuple", "C. array", "D. dictionary"],
            "answer": "C"
        },
        # Add more questions...
    ]

    print("Welcome to the Python Quiz!\n")
    
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q['question']}")
        for option in q['options']:
            print(f"   {option}")
        
        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
    
    print(f"Quiz complete! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
