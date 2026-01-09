from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import DeclarativeBase
from wtforms import StringField, TextAreaField,IntegerField,SubmitField,BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INIT EXTENSIONS
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# MODELS
class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    map_url = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False, default=False)
    has_toilet = db.Column(db.Boolean, nullable=False, default=False)
    has_wifi = db.Column(db.Boolean, nullable=False, default=False)
    can_take_calls = db.Column(db.Boolean, nullable=False, default=False)
    seats = db.Column(db.String(50), nullable=False, default="0")
    coffee_price = db.Column(db.String(50), nullable=False, default="0")

class CafeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    map_url = StringField('Map URL', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = BooleanField('Sockets')
    has_toilets = BooleanField('Toilets')
    has_wifi = BooleanField('WiFi')
    can_take_calls = BooleanField('TakeCalls')
    seats = StringField('Seats', validators=[DataRequired()])
    coffee_price = StringField('Coffee', validators=[DataRequired()])
    submit = SubmitField('Submit')


# ROUTES
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cafe")
def cafes():
    cafe = []
    data = db.session.execute(db.select(Cafe))
    post_data = data.scalars().all()
    for post in post_data:
        cafe.append(post)
    print(cafe)
    return render_template("cafes.html",cafes=cafe)
@app.route("/delete")
def delete():
    particular_cafe_id = request.args.get('id')
    cafe_to_delete = db.get_or_404(Cafe, particular_cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for("cafes"))

@app.route("/add", methods=["GET", "POST"])
def add():
    cafeForm = CafeForm()
    if cafeForm.validate_on_submit():
        new_cafe = Cafe(
            name = request.form.get("name"),
            map_url = request.form.get("map_url"),
            img_url = request.form.get("img_url"),
            location = request.form.get("location"),
            has_sockets = request.form.get("has_sockets"),
            has_wifi = request.form.get("has_wifi"),
            can_take_calls = request.form.get("can_take_calls"),
            seats = request.form.get("seats"),
            coffee_price = '£'+request.form.get("coffee_price")
                        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("cafes"))

    return render_template("add.html",form = cafeForm)


if __name__ == "__main__":
    app.run(debug=True)
