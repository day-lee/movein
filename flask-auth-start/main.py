from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """to associate the coockie with user object"""
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    """ POST: Gets hold of form input data and adds into DB """
    if request.method == "POST":
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        email = request.form.get('email')
        name = request.form.get('name')
        password = hash_and_salted_password

        user = User.query.filter_by(email=email).first()
        """when try to register but user email already on DB, redirect to login"""
        if user:
            flash("Email address already exists. ")
            return redirect(url_for('login'))

        new_user = User(
                email=email,
                name=name,
                password=password,
            )

        """DB CRUD"""
        db.session.add(new_user)
        db.session.commit()

        #return render_template("secrets.html", user=new_user) #NEEDS MODIFICATION LATER
        return redirect(url_for('home'))
    """GET: Returns an empty form to be filled in"""
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):  # (pw from DB, user typed pw-plain text)
            """no user was found in that email address and password not match"""
            flash("Please check your login details and try again")
            return redirect(url_for("login"))
        """correct!"""
        login_user(user)
        return redirect(url_for("secrets"))

    return render_template("login.html")

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form.get('email')
#         password = request.form.get('password')
#
#         user = User.query.filter_by(email=email).first()
#         # Email doesn't exist
#         if not user:
#             flash("That email does not exist, please try again.")
#             return redirect(url_for('login'))
#         # Password incorrect
#         elif not check_password_hash(user.password, password):
#             flash('Password incorrect, please try again.')
#             return redirect(url_for('login'))
#         # Email exists and password correct
#         else:
#             login_user(user)
#             return redirect(url_for('secrets'))
#
#     return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required #users aren't logged in shouldn't do logout
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename='files/cheat_sheet.pdf')



if __name__ == "__main__":
    app.run(debug=True)
