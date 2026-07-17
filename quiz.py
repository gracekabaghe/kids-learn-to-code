print("Quiz time! Let's test what you know.")
questions = ["what color do you mix by mixing blue with yellow? ", 
"how many legs dord s spider have? "]
answers = ["green", "8"]

for i in range(len(questions)):
    reply = input(questions[i] + " ")
    if reply == answers[i]:
        print("Correct")
    else:
        print("Not quite! The answer was " + answers[i])

