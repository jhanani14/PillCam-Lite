from flask import Flask, render_template, request, redirect
import os
from detect import find_best_match, extract_features, DB_FILE
import json
import shutil

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/verify', methods=['POST'])
def verify():
    file = request.files['pill_image']
    if file:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        best_match, score = find_best_match(path)
        result = f"Best match: {best_match}, Score: {score:.2f}"
        return render_template('index.html', result=result)
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        file = request.files['pill_image']
        pill_name = request.form['pill_name']
        if file and pill_name:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            features = extract_features(path)
            # load db
            db = {}
            if os.path.exists(DB_FILE):
                with open(DB_FILE, 'r') as f:
                    db = json.load(f)
            if pill_name not in db:
                db[pill_name] = []
            db[pill_name].append(features)
            with open(DB_FILE, 'w') as f:
                json.dump(db, f, indent=4)
            return f"Pill {pill_name} registered successfully!"
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
