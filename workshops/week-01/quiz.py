def run_quiz():
    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .pyth", "B. .pt", "C. .py", "D. .python"],
            "answer": "C"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. lambda"],
            "answer": "B"
        },
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["A. 6", "B. 8", "C. 9", "D. 23"],
            "answer": "B"
        }
    ]

    score = 0
    total_questions = len(questions)

    print("Welcome to the Python Quiz!")
    print("Choose the correct answer (A, B, C, or D)\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer: ").upper().strip()
        
        if user_answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}")
        print()

    percentage = (score / total_questions) * 100
    print(f"Quiz completed! Your score: {score}/{total_questions} ({percentage:.1f}%)")

if __name__ == "__main__":
    run_quiz()