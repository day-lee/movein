from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#-------SQLAlchemy----
#CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#CREATE TABLE
class Books(db.Model):
    """Creates db Model (Data Structure)"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

def __init__(self, title, author, rating):
   self.title = title
   self.author = author
   self.rating = rating

db.create_all()

@app.route('/')
def home():
    """Returns a list of objects from DB and Passes data to template"""
    all_books = db.session.query(Books).all()  #returns a list holding objs
    print(all_books)
    return render_template("index.html", all_books=all_books)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


    # book_id = request.args.get('id')
    # # DELETE A RECORD BY ID
    # book_to_delete = Book.query.get(book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()
    # return


@app.route("/add", methods=["GET", "POST"])
def add():
    """GET: (before) Returns 'add' template to get input data """
    """POST: (after) Gets hold of input data and Updates them to home"""

    if request.method == "POST":
        #CREATE RECORD
        new_book = Books(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html") #GET: getting input from html form


@app.route('/edit', methods=["GET", "POST"])
def edit():
    """GET: (before)  to render to specific book's editing page"""
    """POST: (after) Updates the rating and Redirects to home to show a new rating"""

    if request.method == "POST":
        #Update
        book_id = request.form["id"]

        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')  #url parameter    e.g. /edit?id=3
    book_selected = Books.query.get(book_id)
    return render_template("edit.html", book=book_selected)

if __name__ == "__main__":
    app.run(debug=True)

