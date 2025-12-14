from flask import Flask,render_template,url_for
import requests
app = Flask(__name__)

response = requests.get('https://api.npoint.io/674f5423f73deab1e9a7')
blog = response.json()
@app.route('/')
def homepage():
    return render_template('index.html',blog=blog)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<blog_id>')
def postpage(blog_id):
    for blog_posts in blog:
        if blog_posts['id'] == int(blog_id):
            requested_post = blog_posts
    return render_template('post.html',post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

