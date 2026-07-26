from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Kids Quiz App</h1><p>Welcome to our quiz app.</p>"

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answer = request.form["answer"]
        if answer == "green":
            return "<h1>Correct!</h1>"
        else:
            return "<h1>Not quite! The answer was green.</h1>"
    else:
        return """
            <h1>What color do you get mixing blue and yellow?</h1>
            <form method="post">
                <input name="answer">
                <button>Submit</button>
            </form>
        """

app.run(debug=True)