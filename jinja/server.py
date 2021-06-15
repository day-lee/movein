from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)


@app.route("/")
def home():
    today_year = datetime.today().year
    return render_template("index.html", today_year=today_year)

@app.route("/guess/<name>")
def guess(name):
    today_year = datetime.today().year
    parameters = {
        "name": name,
    }
    response_gender = requests.get(url="https://api.genderize.io", params=parameters)
    response_gender.raise_for_status()

    gender_data = response_gender.json()
    gender = gender_data['gender']

    parameters = {
        "name": name,
    }
    response_age = requests.get(url="https://api.agify.io", params=parameters)
    response_age.raise_for_status()

    age_data = response_age.json()
    age = age_data['age']
    count = age_data['count']
    return render_template("guess.html", name=name, gender=gender, age=age, count=count, today_year=today_year)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

