import os
import secrets
from datetime import datetime
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# =========================
# CONFIG
# =========================
ADMIN_KEY = "tim"  # CHANGE THIS to your preferred secret

# DB CONFIGURATION
# This handles the switch: Local -> SQLite, Render -> PostgreSQL
uri = os.environ.get("DATABASE_URL", "sqlite:///stations.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)  # Fix for Render/SQLAlchemy compatibility
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# =========================
# DATABASE MODELS
# =========================
class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    verified = db.Column(db.Integer, default=0)  # 0=Pending, 1=Verified
    updated_at = db.Column(db.String(50))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    api_key = db.Column(db.String(100), unique=True)
    role = db.Column(db.String(20), default='public')
    approved = db.Column(db.Integer, default=0)
    applied_at = db.Column(db.String(50))


# Initialize Tables
with app.app_context():
    db.create_all()


# =========================
# HELPERS
# =========================
def generate_api_key():
    return secrets.token_hex(16)


def require_trusted_user():
    api_key = request.headers.get("X-API-KEY")
    if not api_key:
        return None
    user = User.query.filter_by(api_key=api_key).first()
    if not user or user.approved != 1 or user.role not in ["trusted", "admin"]:
        return None
    return user


def require_admin():
    return session.get("admin_authenticated", False)


# =========================
# ROUTES
# =========================
@app.route("/")
def home():
    admin_logged_in = require_admin()
    return render_template("index.html", admin_logged_in=admin_logged_in)


# -------------------------
# ADMIN LOGIN
# -------------------------
@app.route("/admin-login", methods=["POST"])
def admin_login():
    key = request.json.get("key") if request.json else None
    if key == ADMIN_KEY:
        session.permanent = True
        session["admin_authenticated"] = True
        return jsonify({"message": "Access granted"})
    return jsonify({"error": "Forbidden"}), 403


# -------------------------
# ADMIN LOGOUT
# -------------------------
@app.route("/admin-logout")
def admin_logout():
    session.pop("admin_authenticated", None)
    return redirect(url_for("home"))


# -------------------------
# ADMIN DASHBOARD
# -------------------------
@app.route("/admin")
def admin_page():
    if not require_admin():
        return redirect(url_for("home"))

    pending_users = User.query.filter_by(approved=0).all()
    pending_prices = Price.query.filter_by(verified=0).order_by(Price.updated_at.desc()).all()

    return render_template("admin.html", users=pending_users, prices=pending_prices)


# -------------------------
# ADMIN ACTIONS
# -------------------------
@app.route("/admin/approve-user", methods=["POST"])
def approve_user():
    if not require_admin():
        return jsonify({"error": "Forbidden"}), 403
    email = request.json.get("email")
    user = User.query.filter_by(email=email, approved=0).first()
    if not user:
        return jsonify({"error": "User not found or already approved"}), 404

    user.approved = 1
    user.role = 'trusted'
    db.session.commit()
    return jsonify({"message": "User approved as trusted"})


@app.route("/admin/reject-user", methods=["POST"])
def reject_user():
    if not require_admin():
        return jsonify({"error": "Forbidden"}), 403
    email = request.json.get("email")
    user = User.query.filter_by(email=email, approved=0).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User rejected successfully"})


@app.route("/admin/approve-price", methods=["POST"])
def approve_price():
    if not require_admin():
        return jsonify({"error": "Forbidden"}), 403
    price_id = request.json.get("id")
    price_item = Price.query.filter_by(id=price_id, verified=0).first()
    if not price_item:
        return jsonify({"error": "Price not found"}), 404

    price_item.verified = 1
    db.session.commit()
    return jsonify({"message": "Price approved successfully"})


@app.route("/admin/reject-price", methods=["POST"])
def reject_price():
    if not require_admin():
        return jsonify({"error": "Forbidden"}), 403
    price_id = request.json.get("id")
    price_item = Price.query.filter_by(id=price_id, verified=0).first()
    if not price_item:
        return jsonify({"error": "Price not found"}), 404

    db.session.delete(price_item)
    db.session.commit()
    return jsonify({"message": "Price rejected successfully"})


# -------------------------
# PUBLIC SUBMIT
# -------------------------
@app.route("/submit-price", methods=["POST"])
def submit_price():
    data = request.json or {}
    if not all(k in data for k in ("station", "location", "price")):
        return jsonify({"error": "Missing fields"}), 400
    try:
        price_val = float(data["price"])
    except:
        return jsonify({"error": "Price must be a number"}), 400

    new_price = Price(
        station=data["station"],
        location=data["location"],
        price=price_val,
        updated_at=datetime.now().isoformat()
    )
    db.session.add(new_price)
    db.session.commit()
    return jsonify({"message": "Price submitted (Pending verification)"}), 201


# -------------------------
# PUBLIC VIEW
# -------------------------
@app.route("/prices")
def get_prices():
    prices = Price.query.order_by(Price.updated_at.desc()).all()
    # Convert SQL objects to dictionary list
    output = []
    for p in prices:
        output.append({
            "id": p.id,
            "station": p.station,
            "location": p.location,
            "price": p.price,
            "verified": p.verified,
            "updated_at": p.updated_at
        })
    return jsonify(output)


# -------------------------
# APPLY FOR ACCESS
# -------------------------
@app.route("/apply", methods=["POST"])
def apply_for_trust():
    data = request.json or {}
    if not all(k in data for k in ("full_name", "email", "phone", "address")):
        return jsonify({"error": "Missing fields"}), 400

    # Check if exists
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "User already exists"}), 409

    api_key = generate_api_key()
    new_user = User(
        full_name=data["full_name"],
        email=data["email"],
        phone=data["phone"],
        address=data["address"],
        api_key=api_key,
        applied_at=datetime.now().isoformat()
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Application submitted. Await admin approval.", "api_key": api_key})


# -------------------------
# UPDATE PRICE (TRUSTED)
# -------------------------
@app.route("/update-price", methods=["PUT"])
def update_price_trusted():
    user = require_trusted_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json or {}

    price_item = Price.query.get(data.get("id"))
    if not price_item:
        return jsonify({"error": "Price ID not found"}), 404

    price_item.price = data["price"]
    price_item.verified = 1
    price_item.updated_at = datetime.now().isoformat()
    db.session.commit()

    return jsonify({"message": "Price verified and updated", "verified_by": user.email})


# -------------------------
# ADMIN DATA REFRESH
# -------------------------
@app.route("/admin-data")
def admin_data():
    if not require_admin():
        return jsonify({"error": "Forbidden"}), 403

    pending_users = User.query.filter_by(approved=0).all()
    pending_prices = Price.query.filter_by(verified=0).order_by(Price.updated_at.desc()).all()

    # Manual serialization
    users_list = [{
        "full_name": u.full_name,
        "email": u.email,
        "phone": u.phone,
        "address": u.address,
        "applied_at": u.applied_at
    } for u in pending_users]

    prices_list = [{
        "id": p.id,
        "station": p.station,
        "location": p.location,
        "price": p.price,
        "updated_at": p.updated_at
    } for p in pending_prices]

    return jsonify({"users": users_list, "prices": prices_list})


if __name__ == "__main__":
    app.run(debug=True)