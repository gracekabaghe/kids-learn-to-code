# print("Quiz time! Let's test what you know.")
# questions = ["what color do you get by mixing blue with yellow? ", 
# "how many legs does a spider have? "]
# answers = ["green", "8"]

# for i in range(len(questions)):
#     reply = input(questions[i] + " ")
#     if reply == answers[i]:
#         print("Correct")
#     else:
#         print("Not quite! The answer was " + answers[i])

print("Quiz time! Let's test what you know.")
# questions = ["what color do you get by mixing blue with yellow? ", 
# "How many legs does a spider have? "]
# answers = ["green", "8"]

# def ask_question(question, correct_answer):
#     reply = input(question + " ")
#     if reply == correct_answer:
#         print("Correct")
#     else:
#         print("Not quite! The answer was " + correct_answer) 

# for i in range(len(questions)):
#     ask_question(questions[i], answers[i])

quiz = {
    "What color do you get by mixing blue with yello?":
        "Green",
    "How many legs does a spider have?":
        "8"
    }

def ask_question(question, correct_answer):
    reply = input(question + " ")
    if reply == correct_answer:
        print("Correct")
    else:
        print("Not quite! The correct answer was " + correct_answer)

for question, answer in quiz.items():
    ask_question(question, answer)
