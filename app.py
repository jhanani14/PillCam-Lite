from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from models import db, User, History
from auth import auth
from cv_matcher import match_pill
from ocr import extract_text
import config, os

app = Flask(__name__)
app.config.from_object(config)

# Initialize DB
db.init_app(app)

# Login manager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))  # SQLAlchemy 2.0 safe

# Register auth blueprint
app.register_blueprint(auth)

# ---------------- ROUTES ---------------- #

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['image']

        if file.filename == '':
            return redirect(url_for('upload'))

        save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(save_path)

        # CV + OCR
        pill = match_pill(save_path)
        text = extract_text(save_path)

        # Save history
        record = History(
            user_id=current_user.id,
            pill_name=pill,
            ocr_text=text
        )
        db.session.add(record)
        db.session.commit()

        return render_template('result.html', pill=pill, text=text)

    return render_template('upload.html')

@app.route('/history')
@login_required
def history():
    records = History.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html', records=records)

# ---------------- RUN ---------------- #

if __name__ == "__main__":
    os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)

    with app.app_context():
        db.create_all()

    app.run(debug=True)
