from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import sqlite3
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # secure session key

# =========================
# CONFIG
# =========================
ADMIN_KEY = "tim"  # CHANGE THIS to a strong secret

# =========================
# DATABASE
# =========================
def get_db():
    conn = sqlite3.connect("stations.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    # Prices table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station TEXT NOT NULL,
            location TEXT NOT NULL,
            price REAL NOT NULL,
            verified INTEGER DEFAULT 0,
            updated_at TEXT
        )
    """)
    # Users table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            api_key TEXT UNIQUE,
            role TEXT DEFAULT 'public',
            approved INTEGER DEFAULT 0,
            applied_at TEXT
        )
    """)
    conn.commit()
    conn.close()

# Initialize DB at startup
init_db()

# =========================
# HELPERS
# =========================
def generate_api_key():
    return secrets.token_hex(16)

def get_user_by_key(api_key):
    if not api_key:
        return None
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE api_key = ?", (api_key,)).fetchone()
    conn.close()
    return user

def require_trusted_user():
    api_key = request.headers.get("X-API-KEY")
    user = get_user_by_key(api_key)
    if not user or user["approved"] != 1 or user["role"] not in ["trusted","admin"]:
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
        session.permanent = True               # keep session alive
        session["admin_authenticated"] = True
        return jsonify({"message":"Access granted"})
    return jsonify({"error":"Forbidden"}),403

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
    conn = get_db()
    pending_users = conn.execute("SELECT * FROM users WHERE approved=0").fetchall()
    pending_prices = conn.execute("SELECT * FROM prices WHERE verified=0 ORDER BY updated_at DESC").fetchall()
    conn.close()
    return render_template("admin.html", users=pending_users, prices=pending_prices)

# -------------------------
# ADMIN APPROVE/REJECT USER
# -------------------------
@app.route("/admin/approve-user", methods=["POST"])
def approve_user():
    if not require_admin():
        return jsonify({"error":"Forbidden"}),403
    email = request.json.get("email")
    conn = get_db()
    result = conn.execute("UPDATE users SET approved=1, role='trusted' WHERE email=? AND approved=0",(email,))
    conn.commit()
    conn.close()
    if result.rowcount==0:
        return jsonify({"error":"User not found or already approved"}),404
    return jsonify({"message":"User approved as trusted"})

@app.route("/admin/reject-user", methods=["POST"])
def reject_user():
    if not require_admin():
        return jsonify({"error":"Forbidden"}),403
    email = request.json.get("email")
    conn = get_db()
    result = conn.execute("DELETE FROM users WHERE email=? AND approved=0",(email,))
    conn.commit()
    conn.close()
    if result.rowcount==0:
        return jsonify({"error":"User not found or already approved"}),404
    return jsonify({"message":"User rejected successfully"})

# -------------------------
# ADMIN APPROVE/REJECT PRICE
# -------------------------
@app.route("/admin/approve-price", methods=["POST"])
def approve_price():
    if not require_admin():
        return jsonify({"error":"Forbidden"}),403
    price_id = request.json.get("id")
    conn = get_db()
    result = conn.execute("UPDATE prices SET verified=1 WHERE id=? AND verified=0",(price_id,))
    conn.commit()
    conn.close()
    if result.rowcount==0:
        return jsonify({"error":"Price not found or already verified"}),404
    return jsonify({"message":"Price approved successfully"})

@app.route("/admin/reject-price", methods=["POST"])
def reject_price():
    if not require_admin():
        return jsonify({"error":"Forbidden"}),403
    price_id = request.json.get("id")
    conn = get_db()
    result = conn.execute("DELETE FROM prices WHERE id=? AND verified=0",(price_id,))
    conn.commit()
    conn.close()
    if result.rowcount==0:
        return jsonify({"error":"Price not found or already verified"}),404
    return jsonify({"message":"Price rejected successfully"})

# -------------------------
# PUBLIC: Submit Price
# -------------------------
@app.route("/submit-price", methods=["POST"])
def submit_price():
    data = request.json or {}
    if not all(k in data for k in ("station","location","price")):
        return jsonify({"error":"Missing fields"}),400
    try:
        price = float(data["price"])
    except:
        return jsonify({"error":"Price must be a number"}),400

    conn = get_db()
    conn.execute("""
        INSERT INTO prices (station, location, price, updated_at)
        VALUES (?,?,?,?)
    """, (data["station"], data["location"], price, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return jsonify({"message":"Price submitted (Pending verification)"}),201

# -------------------------
# PUBLIC: View Prices
# -------------------------
@app.route("/prices")
def get_prices():
    conn = get_db()
    rows = conn.execute("SELECT * FROM prices ORDER BY updated_at DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

# -------------------------
# APPLY FOR TRUSTED ACCESS
# -------------------------
@app.route("/apply", methods=["POST"])
def apply_for_trust():
    data = request.json or {}
    required_fields = ["full_name","email","phone","address"]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error":f"{field} is required"}),400
    api_key = generate_api_key()
    conn = get_db()
    try:
        conn.execute("""
            INSERT INTO users (full_name,email,phone,address,api_key,applied_at)
            VALUES (?,?,?,?,?,?)
        """, (data["full_name"], data["email"], data["phone"], data["address"], api_key, datetime.now().isoformat()))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error":"User already exists"}),409
    finally:
        conn.close()
    return jsonify({"message":"Application submitted. Await admin approval.","api_key":api_key})

# -------------------------
# UPDATE PRICE (TRUSTED USERS)
# -------------------------
@app.route("/update-price", methods=["PUT"])
def update_price_trusted():
    user = require_trusted_user()
    if not user:
        return jsonify({"error":"Unauthorized"}),401
    data = request.json or {}
    conn = get_db()
    conn.execute("UPDATE prices SET price=?, verified=1, updated_at=? WHERE id=?",
                 (data["price"], datetime.now().isoformat(), data["id"]))
    conn.commit()
    conn.close()
    return jsonify({"message":"Price verified and updated","verified_by":user["email"]})

# =========================
# ADMIN DATA (for auto-refresh panel)
# =========================
@app.route("/admin-data")
def admin_data():
    if not require_admin():
        return jsonify({"error": "Forbidden"}), 403

    conn = get_db()
    pending_users = conn.execute("SELECT * FROM users WHERE approved=0").fetchall()
    pending_prices = conn.execute("SELECT * FROM prices WHERE verified=0 ORDER BY updated_at DESC").fetchall()
    conn.close()

    users_list = [dict(u) for u in pending_users]
    prices_list = [dict(p) for p in pending_prices]

    return jsonify({"users": users_list, "prices": prices_list})

# =========================
# RUN APP
# =========================
if __name__=="__main__":
    app.run(debug=True)
