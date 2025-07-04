
def run_quiz():
    """
    A simple, interactive command-line quiz about Python basics.
    """
    questions = [
        {
            "question": "What is the output of `print(2 ** 3)`?",
            "options": ["a) 6", "b) 8", "c) 9", "d) 12"],
            "answer": "b"
        },
        {
            "question": "Which of the following is used to add an element to the end of a list?",
            "options": ["a) .add()", "b) .push()", "c) .append()", "d) .insert()"],
            "answer": "c"
        },
        {
            "question": "How do you start a single-line comment in Python?",
            "options": ["a) //", "b) #", "c) /*", "d) --"],
            "answer": "b"
        },
        {
            "question": "What is the correct way to create a function in Python?",
            "options": ["a) function myFunction():", "b) create myFunction():", "c) def myFunction():", "d) function = myFunction():"],
            "answer": "c"
        },
        {
            "question": "Which method can be used to remove any whitespace from both the beginning and the end of a string?",
            "options": ["a) .strip()", "b) .trim()", "c) .len()", "d) .ptrim()"],
            "answer": "a"
        }
    ]

    score = 0
    print("--- Welcome to the Python Basics Quiz! ---")

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        while True:
            user_answer = input("Your answer (a, b, c, or d): ").lower()
            if user_answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Invalid input. Please enter a, b, c, or d.")

        if user_answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\n--- Quiz Finished! ---")
    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
