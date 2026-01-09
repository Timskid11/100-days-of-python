from flask import Flask, render_template, request
import os
import numpy as np
from collections import Counter
from PIL import Image
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import FileField, SubmitField
from flask_bootstrap import Bootstrap5

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'rfaerhjflaerkjncbsa,zds'

Bootstrap5(app)


class UploadImage(FlaskForm):
    file = FileField('Upload image', validators=[FileRequired()])
    submit = SubmitField('Upload')


def allowed_file(filename):
    return filename.lower().endswith((".png", ".jpg", ".jpeg"))


def count_colors(img, n):
    pixels = np.array(img).reshape(-1, 3)
    counts = Counter(map(tuple, pixels))
    return counts.most_common(n)

@app.route("/", methods=["GET", "POST"])
def index():
    form = UploadImage()
    colors = None
    img = None  # ✅ initialize here

    if form.validate_on_submit():
        file = form.file.data
        if allowed_file(file.filename):
            img = Image.open(file).convert("RGB")
            colors = count_colors(img, 10)

    return render_template("index.html", form=form, colors=colors, img=img)



if __name__ == "__main__":
    app.run(debug=True)
