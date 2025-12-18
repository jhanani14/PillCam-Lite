# 💊 PillCam-Lite
### Explainable Pill Verification System using Computer Vision and OCR

PillCam-Lite is an end-to-end Computer Vision–based web application that verifies pills using image processing and Optical Character Recognition (OCR). The system allows users to upload pill images, extract text using OCR, and identify pills based on visual and textual cues, while maintaining verification history for traceability.

---

## 🚀 Features

- 🔐 User Authentication (Login & Register)
- 📷 Pill Image Upload
- 🧠 Computer Vision–based preprocessing
- 🔍 OCR-based text extraction (Tesseract)
- 🏷️ Pill Identification Logic
- 📊 Verification History Tracking
- 🖥️ Clean Web Interface (Flask + HTML/CSS)

---

## 🏗️ System Architecture

User → Web UI → Flask Backend
├── CV Processing
├── OCR Extraction
├── Pill Matching Logic
└── Database (SQLite)


---

## 🧪 Technologies Used

| Category | Tools |
|-------|------|
| Backend | Flask (Python) |
| CV | OpenCV |
| OCR | Tesseract OCR |
| Database | SQLite + SQLAlchemy |
| Frontend | HTML, CSS |
| Auth | Flask-Login |

---

## 📂 Project Structure

PillCam-Lite/
├── app.py
├── auth.py
├── models.py
├── cv_matcher.py
├── ocr.py
├── config.py
├── requirements.txt
├── templates/
├── static/
└── uploads/


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/<your-username>/PillCam-Lite.git
cd PillCam-Lite


---

## ⚙️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/<your-username>/PillCam-Lite.git
cd PillCam-Lite

### 2. Create virtual environment

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Install Tesseract OCR

Download from official source

Add installation path to system PATH

Verify:

tesseract --version

### 5. Run the Application

python app.py

Open browser:

http://127.0.0.1:5000

---

## How It Works

1. User uploads pill image

2. Image is preprocessed using OpenCV

3. OCR extracts visible text from pill

4. Matching logic identifies pill

5. Result and OCR text are displayed

6. Verification is stored in history.

---

## Future Enhancements (Version 3)

1. Confidence score calculation

2. Dataset-based validation

3. Advanced CV feature extraction

4. False positive handling

5. UI/UX improvements

6. Performance evaluation metrics