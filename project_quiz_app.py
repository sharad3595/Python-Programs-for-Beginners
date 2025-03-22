import random

# List of questions with options and correct answers
quiz_data = [
    {
        "question": "Which city is the capital of Nepal?",
        "options": ["A) Hetauda", "B) Kathmandu", "C) Chitwan", "D) Humla"],
        "answer": "B"
    },
    {
        "question": "Which programming language is known for data science?",
        "options": ["A) Java", "B) C++", "C) Python", "D) Swift"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A) 5", "B) 8", "C) 7", "D) 10"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    }
]


# Function to run the quiz
def run_quiz():
    score = 0
    total_questions = len(quiz_data)
    random.shuffle(quiz_data)  # Randomize questions
    
    for idx, question in enumerate(quiz_data, start=1):
        print(f"\n Question {idx}: {question['question']}")
        for option in question["options"]:
            print(option)

        user_answer = input("\n Enter your answer (A/B/C/D): ").strip().upper()
        
        if user_answer == question["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Incorrect! The correct answer was {question['answer']}.")

    print("\n Quiz Completed!")
    print(f" Your final score: {score} / {total_questions}")
    
#  Start the quiz
run_quiz()
