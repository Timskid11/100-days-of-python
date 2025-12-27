from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load .env file only if it exists (for local development)
load_dotenv()

app = Flask(__name__)
# Get SECRET_KEY from environment (Render) or use dev key (Local)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-for-local')

# --- DATABASE SETUP (The "Smart" Switch) ---
# 1. Try to get the database URL from the environment (Render provides this)
db_url = os.environ.get('DATABASE_URL')

if db_url:
    # 2. If we are on Render, use Postgres
    # Fix Render's URL quirk (postgres:// -> postgresql://)
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    print("Using PRODUCTION Database (Postgres)")
else:
    # 3. If no URL is found, we are on your laptop. Use SQLite.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
    print("Using LOCAL Database (SQLite)")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)

# --- LOGIN SETUP ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --- DATABASE MODELS ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(250), nullable=False)


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    image = db.Column(db.String(200))


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(100))
    description = db.Column(db.Text)


# --- DATABASE SEEDING ---
# This runs every time the app starts to ensure tables exist
with app.app_context():
    db.create_all()
    # Create default sections if they are missing
    if not Section.query.filter_by(name='intro').first():
        intro = Section(name='intro', title="I'm Timilehin", content="I am a Python Developer...", image="me.jpg")
        about = Section(name='about', title="About Me", content="Security Engineering in AI...", image="bg.jpg")
        db.session.add(intro)
        db.session.add(about)
        db.session.commit()


# --- ROUTES ---

@app.route('/')
def home():
    projects = Project.query.all()
    experiences = Experience.query.all()
    sections_list = Section.query.all()
    sections = {section.name: section for section in sections_list}

    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    # Handle IP logic safely (in case behind proxy)
    if request.headers.getlist("X-Forwarded-For"):
        user_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        user_ip = request.remote_addr

    return render_template("index.html",
                           projects=projects,
                           sections=sections,
                           experiences=experiences,
                           greeting=greeting,
                           ip=user_ip)


@app.route('/contact', methods=["POST"])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Get credentials from Environment Variables (Render)
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    # You can put these in env vars too, but hardcoding is OK for personal projects
    twilio_phone = "+12176018679"
    my_phone = "+2348104599093"

    try:
        client = Client(account_sid, auth_token)
        sms = client.messages.create(
            body=f"🚀 LEAD: {name}\n📧 {email}\n💬 {message}",
            from_=twilio_phone,
            to=my_phone
        )
        print(f"SMS Sent! ID: {sms.sid}")
        flash("Message sent! I'll get back to you soon.")
    except Exception as e:
        print(f"Twilio Error: {e}")
        # flash(f"Error: {e}") # Uncomment for debugging
        flash("Message sent locally (SMS failed).")

    return redirect(url_for('home'))


# --- AUTH ROUTES ---

@app.route('/register', methods=["GET", "POST"])
def register():
    # Use this ONCE to create your admin account, then comment out the logic inside
    if request.method == "POST":
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'), method='pbkdf2:sha256', salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            flash("That email already exists.")
            return redirect(url_for('register'))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Incorrect email or password.")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template("login.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# --- EDIT ROUTES ---

@app.route('/add-project', methods=["GET", "POST"])
@login_required
def add_project():
    if request.method == "POST":
        file = request.files['image']
        filename = secure_filename(file.filename)
        # Ensure uploads folder exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_project = Project(
            title=request.form.get("title"),
            description=request.form.get("description"),
            img_url=filename,
            link=request.form.get("link")
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add_project.html")


@app.route('/add-experience', methods=["GET", "POST"])
@login_required
def add_experience():
    if request.method == "POST":
        new_job = Experience(
            company=request.form.get("company"),
            role=request.form.get("role"),
            duration=request.form.get("duration"),
            description=request.form.get("description")
        )
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add_experience.html")


@app.route('/edit-section/<section_name>', methods=["GET", "POST"])
@login_required
def edit_section(section_name):
    section = Section.query.filter_by(name=section_name).first()
    if request.method == "POST":
        section.title = request.form.get("title")
        section.content = request.form.get("content")
        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                filename = secure_filename(file.filename)
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                section.image = filename
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit_section.html", section=section)


if __name__ == "__main__":
    app.run(debug=True)