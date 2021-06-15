# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# 
# # cursor.execute("CREATE TABLE books (
# id INTEGER PRIMARY KEY,
# title varchar(250) NOT NULL UNIQUE,
# author varchar(250) NOT NULL,
# rating FLOAT NOT NULL)")
# 
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

def __init__(self, title, author, rating):
   self.title = title
   self.author = author
   self.rating = rating

db.create_all()

# book_1 = Books(title='Harry Porter', author='J. K. Rowling', rating=9.3)
# db.session.add(book_1)
#
# book_2 = Books(title='Harry Porter and Friends', author='J. K. Rowling', rating=9.1)
# db.session.add(book_2)
#
# db.session.commit()
#
# book_id = 1
# book_to_delete = Books.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
# all_books = db.session.query(Books).all()
# print(all_books)
# print(all_books[0].title)

#
book_id = 2
book_to_update = Books.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()