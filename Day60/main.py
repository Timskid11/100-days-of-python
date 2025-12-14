import os

from flask import Flask, render_template,request
import requests
import smtplib
from dotenv import load_dotenv
load_dotenv()
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
password = os.getenv("password")
app = Flask(__name__)



@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/contact',methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        entry = request.form
        print(entry['name'])
        print(entry['email'])
        print(entry['phone'])
        print(entry['message'])
        connect = smtplib.SMTP('smtp-mail.outlook.com', 587)
        connect.starttls()
        connect.login(user='timilehinoyinlola3@gmail.com', password=password)
        connect.sendmail(from_addr='timilehinoyinlola3@gmail.com', to_addrs='oyinlolarobot@gmail.com',
                         msg=f"Subject: Happy Birthday!!!\n\nName : {entry['name']} \n Email: {entry['email']} \n Phone: {entry['phone']} \n {entry['message']}")
        return render_template("contact.html", contact_status="Successfully sent message")

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
