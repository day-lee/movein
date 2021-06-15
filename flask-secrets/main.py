from flask import Flask, render_template, url_for, redirect

"""Form object declaration"""
from flask_wtf import FlaskForm

from wtforms import StringField, TextField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    """Login Form"""
    email = StringField(label='Email', validators=[
        Email(message=('Not a valid email address.')),
        DataRequired()
    ])

    password = PasswordField(label='Password', validators=[
        Length(min=8,
        message=('Your password is too short.')),
        DataRequired()
    ])

    login = SubmitField('Login')



app = Flask(__name__)
app.secret_key = "secret i am"
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    """Standard `login` form."""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html", form=login_form)
    return render_template("login.html", form=login_form)



if __name__ == '__main__':
    app.run(debug=True)