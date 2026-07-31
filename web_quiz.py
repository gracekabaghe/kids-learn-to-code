from flask import Flask, request, redirect, render_template

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
    a { display: inline-block; margin-top: 20px; padding: 12px 30px; color: white; text-decoration: none; border-radius: 5px; font-size: 18px; }
    .correct { background: #2ecc71; color: white; padding: 20px; border-radius: 10px; font-size: 24px; }
    .wrong { background: #e74c3c; color: white; padding: 20px; border-radius: 10px; font-size: 24px; }
    .score { font-size: 24px; font-weight: bold; color: #e74c3c; }
"""

@app.route("/")
def home():
    total = len(questions)
    return render_template("home.html", total = total)

@app.route("/quiz", methods=["GET", "POST"])
def quiz_page():
    q = int(request.args.get("q", 0))
    score = int(request.args.get("score", 0))

    if request.method == "POST":
        answer = request.form["answer"]
        correct = answers[q]
        is_right = answer.lower() == correct.lower()

        if is_right:
            score = score + 1
            feedback = f'<div class="correct">✅ Correct!</div>'
        else:
            feedback = f'<div class="wrong">❌ Not quite! The answer was: <b>{correct}</b></div>'

        if q + 1 < len(questions):
            next_link = f'<a href="/quiz?q={q + 1}&score={score}" class="correct">Next Question ➡️</a>'
            return f"""
                <html><head><style>{STYLE}</style></head><body>
                {feedback}
                <p style="margin-top:20px;">Score: {score} / {q + 1}</p>
                {next_link}
                </body></html>
            """
        else:
            return f"""
                <html><head><style>{STYLE}</style></head><body>
                {feedback}
                <p style="margin-top:20px;">Final Score:</p>
                <p class="score">{score} out of {len(questions)}</p>
                <a href="/" class="correct">Try Again</a>
                </body></html>
            """

    if q < len(questions):
        return f"""
            <html><head><style>{STYLE}</style></head><body>
            <h1>Question {q + 1} of {len(questions)}</h1>
            <p style="font-size: 22px; color: #333;">{questions[q]}</p>
            <form method="post">
                <input name="answer" autofocus placeholder="Type your answer...">
                <button>Submit</button>
            </form>
            <p style="margin-top:15px; color:#999;">Score: {score}</p>
            </body></html>
        """
@app.route("/about")
def about():
    return f"""
    <html><head><style>{STYLE}</style></head><body>
    <h2>This quiz was built by Grace while learning Python. </h2>
    <a href="/">Home</a>
    """

app.run(debug=True)