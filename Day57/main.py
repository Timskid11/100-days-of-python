import requests
from flask import Flask, render_template,url_for



app = Flask(__name__)
response = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')


@app.route('/')
def home():
    content = response.json()
    return render_template("index.html",content=content)

@app.route('/post/<blog_id>')
def read_post(blog_id):
    content = response.json()
    return render_template("post.html", blog_id=int(blog_id), posts=content)


if __name__ == "__main__":
    app.run(debug=True)
