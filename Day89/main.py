from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, TextAreaField,IntegerField,SubmitField,BooleanField
from wtforms.validators import DataRequired
from sqlalchemy import Integer, String


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do.db'
Bootstrap5(app)
app.config['SECRET_KEY'] = 'rfaerhjflaerkjncbsa,zds'


# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class To_Do(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    to_do: Mapped[str] = mapped_column(String(1000))
'''
with app.app_context():
    db.create_all()
'''

class add_to_do(FlaskForm):
    to_do = StringField('To-Do')

@app.route('/',methods=['GET','POST'])
def index():
    form = add_to_do()
    if form.validate_on_submit():
        new_to_do = To_Do(to_do=form.to_do.data)
        db.session.add(new_to_do)
        db.session.commit()
        return redirect(url_for('index'))
    data = db.session.execute(db.select(To_Do).order_by(To_Do.id))
    db_data = data.scalars().all()
    return render_template('index.html',form=form,database = db_data)

@app.route('/delete')
def delete_task():
    id = request.args.get('task_id')
    db_to_delete = db.get_or_404(To_Do,id)
    db.session.delete(db_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)