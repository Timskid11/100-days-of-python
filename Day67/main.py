from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from sqlalchemy.testing.config import any_async
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Body Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


@app.route('/')
def get_all_posts():
    posts = []
    data = db.session.execute(db.select(BlogPost).order_by(BlogPost.id))
    post_data = data.scalars().all()
    for post in post_data:
        posts.append(post)
    return render_template("index.html", all_posts=posts)


@app.route('/post/<post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)



@app.route('/new-post',methods=["GET","POST"])
def add_new_post():
    blog_form = BlogPostForm()
    if blog_form.validate_on_submit():
        new_post = BlogPost(
            title=blog_form.title.data,
            subtitle=blog_form.subtitle.data,
            body=blog_form.body.data,
            img_url=blog_form.img_url.data,
            author=blog_form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html",form=blog_form,h_element = "New Post")

@app.route('/edit-post/<post_id>',methods=["GET","POST"])
def edit_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    form = BlogPostForm(obj=requested_post)
    if form.validate_on_submit():
        requested_post.title = form.title.data
        requested_post.subtitle = form.subtitle.data
        requested_post.body = form.body.data
        requested_post.img_url = form.img_url.data
        requested_post.author = form.author.data
        requested_post.date = date.today().strftime("%B %d, %Y")
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html",form=form,h_element = "Edit Post")

@app.route('/delete-post/<post_id>',methods=["GET","POST"])
def delete_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    db.session.delete(requested_post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
