from quiz_data import build_quiz
from ask import ask_question

print("Quiz time! Let's test what you know.")

quiz = build_quiz("questions.txt")

score = 0
for question, answer in quiz.items():
    if ask_question(question, answer):
        score = score + 1

print("You got", score, "out of", len(quiz))