from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"


if __name__ == "__main__":
    from webbrowser import open
    open("http://127.0.0.1:5000")

    app.run()
