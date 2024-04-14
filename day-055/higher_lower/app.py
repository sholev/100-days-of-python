from flask import Flask
from random import randint

app = Flask(__name__)

START_GIF = "https://media4.giphy.com/media/IsfrRWvbUdRny/giphy.gif"
HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"


@app.route('/')
def home():
    global number
    number = randint(1, 9)
    return (f'<h1 style="color:black">{'Guess a number between 0 and 9'}</h1>'
            f'<br><img src="{START_GIF}">')


@app.route('/<int:n>')
def guess(n):
    if n < number:
        return (f'<h1 style="color:red">Too low, try again!</h1>'
                f'<br><img src="{LOW}">')
    elif n > number:
        return (f'<h1 style="color:purple">Too high, try again!</h1>'
                f'<br><img src="{HIGH}">')

    return (f'<h1 style="color:green">You found me!</h1>'
            f'<br><img src="{CORRECT}">')


if __name__ == '__main__':
    number = -1
    app.run(debug=True)
