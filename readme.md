# 💊 PillCam-Lite  
### Lightweight Pill Identification & OCR System for Healthcare Applications

---

## 📌 Abstract
Accurate identification of pharmaceutical pills and extraction of imprint text from images is challenging due to variations in pill shape, color, imprint clarity, lighting conditions, and camera quality. Existing systems mostly rely on deep learning models that require large labeled datasets, high computational resources, and limited explainability.

**PillCam-Lite** proposes a **lightweight, interpretable, and modular computer vision system** that integrates image preprocessing, visual feature extraction, OCR-based text recognition, and a deterministic feature-fusion scoring algorithm for reliable pill identification. The system is suitable for academic research, healthcare applications, and resource-constrained environments.

---

## 🧠 System Architecture

User Image
↓
Image Preprocessing
↓
Feature Extraction (ORB + HSV)
↓
OCR Text Extraction
↓
Similarity Computation
↓
Weighted Feature Fusion
↓
Pill Identification Result

---

## 🔬 Technologies Used

- Python  
- Flask  
- OpenCV  
- ORB Feature Descriptors  
- Tesseract OCR  
- SQLite  
- NumPy  
- Matplotlib (Evaluation)

---

## 🧪 Methodology

### 1️⃣ Image Preprocessing
- Gaussian blur for noise reduction  
- Adaptive thresholding for segmentation  
- Morphological operations for contour refinement  

### 2️⃣ Visual Feature Extraction
- ORB keypoints and descriptors  
- Fixed-length feature vector generation  

### 3️⃣ Color Feature Representation
- HSV color histogram  
- Histogram normalization  

### 4️⃣ OCR-Based Text Extraction
- Tesseract OCR to extract pill imprints  
- Text cleaning and normalization  

### 5️⃣ Similarity Computation
- Euclidean distance for visual similarity  
- Levenshtein distance for text similarity  

### 6️⃣ Weighted Feature Fusion (Novel Contribution)
A deterministic scoring mechanism combines:
- Visual similarity  
- Color similarity  
- OCR text similarity  

The pill with the **highest combined score** is selected as the final match.

---

## 📊 Evaluation Strategy

### Metrics Used
- Top-1 Identification Accuracy  
- Average Feature Distance  
- OCR Similarity Score  
- Processing Time per Image  

### Evaluation Dataset
- Reference pill images  
- Query images under different lighting, angles, and resolutions  

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

git clone https://github.com/jhanani14/PillCam-Lite.git
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

---

## Key Contributions

Lightweight pill identification without deep learning

Fully interpretable and explainable feature fusion

No dependency on large labeled datasets

Modular and extensible architecture

---

## Application Areas

Medical pill identification

Pharmacy automation systems

Clinical decision support

Healthcare informatics research

---

## References

R. Szeliski, Computer Vision: Algorithms and Applications

R. Gonzalez and R. Woods, Digital Image Processing

C. Bishop, Pattern Recognition and Machine Learning

D. Lowe, “Distinctive Image Features from Scale-Invariant Keypoints”

R. Smith, “An Overview of the Tesseract OCR Engine”

---

## Future Enhancements

Deep learning hybrid comparison

Mobile deployment

Larger reference dataset

Real-time camera integration

