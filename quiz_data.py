def build_quiz(filename):
    quiz = {}
    file = open(filename, "r")
    for line in file:
        parts = line.split("|")
        if len(parts) == 2:
            question = parts[0].strip()
            answer = parts[1].strip()
            quiz[question] = answer
    file.close()
    return quiz