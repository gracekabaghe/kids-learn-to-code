from flask import Flask, request, redirect

app = Flask(__name__)

from quiz_data import build_quiz
quiz = build_quiz("questions.txt")
questions = list(quiz.keys())
answers = list(quiz.values())

@app.route("/")
def home():
    total = len(questions)
    return f"<h1>Kids Quiz App</h1><p>{total} questions ready!</p><a href='/quiz?q=0&score=0'>Start Quiz</a>"

@app.route("/quiz", methods=["GET", "POST"])
def quiz_page():
    q = int(request.args.get("q", 0))
    score = int(request.args.get("score", 0))

    if request.method == "POST":
        answer = request.form["answer"]
        correct = answers[q]
        if answer.lower() == correct.lower():
            score = score + 1
        return redirect(f"/quiz?q={q + 1}&score={score}")

    if q < len(questions):
        return f"""
            <h1>Question {q + 1} of {len(questions)}</h1>
            <p>{questions[q]}</p>
            <form method="post">
                <input name="answer" autofocus>
                <button>Submit</button>
            </form>
        """
    else:
        return f"""
            <h1>Quiz Complete!</h1>
            <p>You got {score} out of {len(questions)}</p>
            <a href="/">Try Again</a>
        """

app.run(debug=True)