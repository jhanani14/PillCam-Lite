import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_required, current_user

from models import db, User, History
from auth import auth
from cv.matcher import match_pill
from ocr.ocr_engine import extract_text
import config

# ---------------- APP INIT ---------------- #

app = Flask(__name__)
app.config.from_object(config)

# Ensure upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# ---------------- DATABASE ---------------- #

db.init_app(app)

# ---------------- LOGIN MANAGER ---------------- #

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))  # SQLAlchemy 2.0 safe

# ---------------- BLUEPRINTS ---------------- #

app.register_blueprint(auth)

# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return redirect(url_for("auth.login"))

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":

        if "image" not in request.files:
            flash("No file uploaded", "danger")
            return redirect(request.url)

        file = request.files["image"]

        if file.filename == "":
            flash("No selected file", "warning")
            return redirect(request.url)

        # Save file
        filename = file.filename
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(path)

        # ---------------- AI PROCESSING ---------------- #
        pill_name = match_pill(path)
        ocr_text = extract_text(path)

        # ---------------- SAVE HISTORY ---------------- #
        record = History(
            user_id=current_user.id,
            pill_name=pill_name,
            ocr_text=ocr_text
        )
        db.session.add(record)
        db.session.commit()

        return render_template(
            "result.html",
            pill=pill_name,
            text=ocr_text,
            image=filename
        )

    return render_template("upload.html")

@app.route("/history")
@login_required
def history():
    records = History.query.filter_by(user_id=current_user.id).order_by(
        History.id.desc()
    ).all()
    return render_template("history.html", records=records)

# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
