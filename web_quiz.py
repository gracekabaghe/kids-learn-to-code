from flask import Flask, request, redirect

app = Flask(__name__)

from quiz_data import build_quiz
quiz = build_quiz("questions.txt")
questions = list(quiz.keys())
answers = list(quiz.values())

STYLE = """
    body { font-family: Arial, sans-serif; text-align: center; padding: 30px; background: #f0f8ff; }
    h1 { color: #2c3e50; }
    p { font-size: 18px; color: #555; }
    input { padding: 10px; font-size: 18px; border: 2px solid #3498db; border-radius: 5px; width: 200px; }
    button { padding: 10px 25px; font-size: 18px; background: #2ecc71; color: white; border: none; border-radius: 5px; cursor: pointer; margin-left: 10px; }
    button:hover { background: #27ae60; }
    a { display: inline-block; margin-top: 20px; padding: 12px 30px; background: #3498db; color: white; text-decoration: none; border-radius: 5px; font-size: 18px; }
    a:hover { background: #2980b9; }
    .score { font-size: 24px; font-weight: bold; color: #e74c3c; }
"""

@app.route("/")
def home():
    total = len(questions)
    return f"""
        <html><head><style>{STYLE}</style></head><body>
        <h1>🐍 Kids Quiz App</h1>
        <p>{total} questions ready!</p>
        <a href='/quiz?q=0&score=0'>Start Quiz</a>
        </body></html>
    """

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
            <html><head><style>{STYLE}</style></head><body>
            <h1>Question {q + 1} of {len(questions)}</h1>
            <p style="font-size: 22px; color: #333;">{questions[q]}</p>
            <form method="post">
                <input name="answer" autofocus placeholder="Type your answer...">
                <button>Submit</button>
            </form>
            </body></html>
        """
    else:
        return f"""
            <html><head><style>{STYLE}</style></head><body>
            <h1>🎉 Quiz Complete!</h1>
            <p class="score">You got {score} out of {len(questions)}</p>
            <a href="/">Try Again</a>
            </body></html>
        """

app.run(debug=True)