from os import urandom
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from login_form import LoginForm

app = Flask(__name__)
app.secret_key = urandom(32)
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (form.username.data == "secret@email.com" and
                form.password.data == "verysecret"):
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
