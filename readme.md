# 💊 PillCam-Lite  
**AI-Based Pill Identification and OCR System**

PillCam-Lite is an AI-powered web application designed to identify pills from images and extract textual information using computer vision and OCR techniques. The system is built using Flask and classical computer vision methods, making it lightweight, interpretable, and suitable for academic research, prototyping, and healthcare-related applications.

---

## 🚀 Key Features

- 🔐 User Authentication (Register / Login)
- 📷 Pill Image Upload
- 🧠 Pill Identification using ORB Feature Matching
- 📝 OCR-based Text Extraction from Pill Images
- 📊 Evaluation Module with Accuracy & Metrics
- 🗂 User History Tracking
- 📈 Confusion Matrix Visualization

---

## 🧠 System Architecture

User
↓
Web Interface (Flask + HTML/CSS)
↓
Image Upload
↓
Preprocessing (OpenCV)
↓
Feature Extraction (ORB)
↓
Feature Matching (Reference DB)
↓
Pill Identification
↓
OCR (Tesseract)
↓
Result + History Storage (SQLite)

---

## 🧪 Technologies Used

| Component | Technology |
|--------|------------|
| Backend | Python, Flask |
| Frontend | HTML, CSS |
| Database | SQLite, SQLAlchemy |
| Computer Vision | OpenCV (ORB) |
| OCR | Tesseract OCR |
| Evaluation | NumPy, scikit-learn, Matplotlib |
| Authentication | Flask-Login |

---

## 📁 Project Structure

PillCam-Lite/
│
├── app.py
├── auth.py
├── config.py
├── models.py
│
├── cv/
│ ├── preprocess.py
│ ├── feature_extractor.py
│ └── matcher.py
│
├── ocr/
│ └── ocr_engine.py
│
├── evaluation/
│ ├── evaluate.py
│ └── confusion_matrix.png
│
├── tools/
│ └── generate_reference.py
│
├── data/
│ ├── raw/images/
│ └── reference_db/features.pkl
│
├── templates/
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── upload.html
│ ├── result.html
│ └── history.html
│
├── static/
│ └── css/style.css
│
├── uploads/
├── requirements.txt
├── README.md
└── .gitignore

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

### 4. Generate Reference Features
python -m tools.generate_reference

### 5. Run the Application
python app.py


### 6. Open browser:

http://127.0.0.1:5000

### 7. Evaluation & Metrics

Run evaluation module:

python -m evaluation.evaluate

### Metrics Used:

Accuracy

Precision

Recall

Confusion Matrix

### Output:

evaluation/confusion_matrix.png

Console metric report

## Future Enhancements

CNN-based pill classification

Top-K matching

Mobile app integration

Multilingual OCR

Drug database API integration