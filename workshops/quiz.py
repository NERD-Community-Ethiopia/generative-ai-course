def run_quiz():
    questions = {
        "What is the capital of France?": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "What is 2 + 2?": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "What color do you get when you mix red and white?": ["A) Pink", "B) Blue", "C) Green", "D) Yellow"],
    }
    
    answers = {
        "What is the capital of France?": "C",
        "What is 2 + 2?": "B",
        "What color do you get when you mix red and white?": "A",
    }

    score = 0

    for question in questions:
        print(question)
        for option in questions[question]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == answers[question]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answers[question]}.\n")
    
    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()