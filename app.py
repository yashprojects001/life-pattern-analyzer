from flask import Flask, render_template, request
from analyzer import analyze_life_pattern

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        sleep = float(request.form["sleep"])
        screen = float(request.form["screen"])
        work = float(request.form["work"])
        mood = int(request.form["mood"])

        result = analyze_life_pattern(sleep, screen, work, mood)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
