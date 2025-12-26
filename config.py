import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Flask
SECRET_KEY = "pillcam_secret_key"
DEBUG = True

# Database
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database", "app.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Uploads
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

# 🔹 TESSERACT PATH (VERY IMPORTANT)
# If installed normally on Windows, this is correct:
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
