from flask import Flask
app = Flask(__name__)


def make_bold(func):
    def add_tag():
        return f"<b>{func()}</b>"
    return add_tag


def make_italic(func):
    def add_tag():
        return f"<em>{func()}</em>"
    return add_tag


def make_underline(func):
    def add_tag():
        return f"<u>{func()}</u>"
    return add_tag


@app.route('/')
@make_bold
@make_italic
@make_underline
def hello_world():
    return "Hello world!"


@app.route('/bye')
def bye():
    return "Bye!"


@app.route('/username/<name>')
def greet(name):
    return f"Hello there {name}!"


@app.route('/username/<name>/<int:number>')
def greet_number(name, number):
    return f"Hello there {name}, you are number {number}!"


if __name__ == "__main__":
    app.run(debug=True)
