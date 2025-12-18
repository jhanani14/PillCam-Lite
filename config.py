import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "pillcam_secret_key_v2"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database", "app.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
