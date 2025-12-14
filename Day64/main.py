from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField
from wtforms.validators import DataRequired,Length
import requests
import os
from dotenv import load_dotenv

load_dotenv()
MOVIE_API_KEY = os.getenv('API_KEY')
url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
MOVIE_DB_INFO_URL="https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL="https://image.tmdb.org/t/p/w500"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String,nullable=False,unique=True)
    year: Mapped[int] = mapped_column(Integer,nullable=False)
    description: Mapped[str] = mapped_column(String,nullable=False)
    rating: Mapped[float] = mapped_column(Float,nullable=True)
    ranking: Mapped[int] = mapped_column(Integer,nullable=True)
    review: Mapped[str] = mapped_column(String,nullable=True)
    img_url: Mapped[str] = mapped_column(String,nullable=False)



with app.app_context():
    db.create_all()
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )
    second_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )

#place for my form

class MovieForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired(),Length(min=1, max=75)])
    submit = SubmitField('Submit')

class NewMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():

    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    selected_movies = result.scalars().all()
    for i in range(len(selected_movies)):
        selected_movies[i].ranking = len(selected_movies) - i
    db.session.commit()


    return render_template("index.html", movies=selected_movies)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    edit_form = MovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if edit_form.validate_on_submit():
        movie.rating = edit_form.rating.data
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form,movie=movie)

@app.route("/delete", methods=["GET", "POST"])
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    new_mform = NewMovieForm()
    if new_mform.validate_on_submit():
        headers = {"accept": "application/json"}
        parameters = {"api_key": MOVIE_API_KEY,
                      "query": new_mform.title.data,}
        response = requests.get(url, headers=headers,params=parameters)
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html",form=new_mform)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_API_KEY, "language": "en-US"})
        data = response.json()

        # Safely handle missing data
        poster_path = data.get("poster_path")
        img_url = f"{MOVIE_DB_IMAGE_URL}{poster_path}"
        print(img_url)
        release_date = data.get("release_date")
        year = int(release_date.split("-")[0]) if release_date else None

        new_movie = Movie(
            title=data.get("title", "No Title"),
            year=year,
            img_url=img_url,
            description=data.get("overview", "No Description"),
            rating=0,
            ranking=0,
            review="No review yet"
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
