from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google(URL)',validators=[DataRequired(),URL()])
    opening_time = StringField(label='Opening Time e.g. 8AM',validators=[DataRequired()])
    closing_time= StringField(label='Closing Time e.g. 5:30PM)',validators=[DataRequired()])
    coffee = SelectField(
        label='Coffee Rating',
        validators=[DataRequired()],
        choices=[
            ('✘', '✘'),
            ('☕️', '☕️'),
            ('☕️☕️', '☕️☕️'),
            ('☕️☕️☕️', '☕️☕️☕️'),
            ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
            ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'),
        ]
    )

    wifi = SelectField(
        label='Wifi Strength Rating',
        validators=[DataRequired()],
        choices=[
            ('✘', '✘'),
            ('💪', '💪'),
            ('💪💪', '💪💪'),
            ('💪💪💪', '💪💪💪'),
            ('💪💪💪💪', '💪💪💪💪'),
            ('💪💪💪💪💪', '💪💪💪💪💪'),
        ]
    )

    power = SelectField(
        label='Power Socket Availability',
        validators=[DataRequired()],
        choices=[
            ('✘', '✘'),
            ('🔌', '🔌'),
            ('🔌🔌', '🔌🔌'),
            ('🔌🔌🔌', '🔌🔌🔌'),
            ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
            ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'),
        ]
    )

    submit = SubmitField(label='Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        #
        with open('./cafe-data.csv', newline='', encoding='utf-8', mode='a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                form.cafe.data,
                form.location.data,
                form.opening_time.data,
                form.closing_time.data,
                form.coffee.data,
                form.wifi.data,
                form.power.data
            ])
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('./cafe-data.csv', newline='', encoding='utf-8',mode='r') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
