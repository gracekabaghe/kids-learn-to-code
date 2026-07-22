def ask_question(question, correct_answer):
    reply = ""
    while reply == "":
        reply = input(question + " ")
        if reply == "":
            print("Please type an answer!")
    if reply == correct_answer:
        print("Correct!")
        return True
    else:
        print("Not quite! The correct answer was " + correct_answer)
        return False