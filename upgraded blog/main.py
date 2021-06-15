from flask import Flask, render_template, request
import requests
from datetime import datetime
from posts import Post
import smtplib

app = Flask(__name__)
#for footer
today_year = datetime.today().year

posts = requests.get(url="https://api.npoint.io/43644ec4f0013682fc0d").json()
post_objects = []
for post in posts:
    post_obj = Post(title=post["title"], subtitle=post["subtitle"], author=post["author"], dates=post["date"], id=post["id"],
                    image=post["image_url"], body=post['body'])
    post_objects.append(post_obj)
#[<post.Post object at 0x0000000003BC3DA0>, <post.Post object at 0x0000000003BC3240>, <post.Post object at 0x0000000003BC3128>]


@app.route("/")
def home():
    return render_template("index.html",  all_posts=post_objects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == 'POST':
        data = request.form
        name = data["name"]
        email = data["email"]
        phone= data["phone"]
        msg = data["message"]


        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@ app.route("/post/<int:index>")
def show_post(index):
    """Passes post object as requested_post, only when its id matches with index from url"""
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# @app.route("/form-entry", methods=["GET", "POST"])
# def receive_data():
#
#     name = request.form['name']
#     email = request.form['email']
#     phone_number = request.form['phonenumber']
#     message = request.form['message']
#     print(name)
#     print(email)
#     print(phone_number)
#     print(message)
#
#     return f"<h1>{name}, Successfully sent your message. </h1>"

if __name__ == "__main__":
    app.run(debug=True)