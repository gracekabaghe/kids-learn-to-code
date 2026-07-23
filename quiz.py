from quiz_data import build_quiz
from ask import ask_question

print("Quiz time! Let's test what you know.")
print("=" * 35)

quiz = build_quiz("questions.txt")
print("choose a mode:")
print("1 - Quiz (you type the answer)")
print("2 - Flashcards (Question then reveal)")
print("-" * 35)
mode = input("Enter 1 or 2")

if mode == "1":
    score = 0
    for question, answer in quiz.items():
        if ask_question(question, answer):
            score = score + 1
    print("🏆  You got", score, "out of", len(quiz), " 🏆")

elif mode == "2":
    for question, answer in quiz.items():
        print("QUESTION:", question)
        input("Press Enter to see the answer...")
        print("ANSWER:", answer)
        print("=" * 35)
        
        print("=" * 35)

else:
    print("That's not 1 or 2. Please restart the quiz.")