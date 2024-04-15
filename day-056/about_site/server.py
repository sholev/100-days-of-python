from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/assets/css/<file>")
def css(file):
    return redirect(f"/static/css/{file}")


if __name__ == "__main__":
    app.run(debug=True)
