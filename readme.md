# PillCam-Lite (v1.0)
### Traditional Computer Vision–Based Pill Verification System

---

## 📌 Project Overview

**PillCam-Lite v1.0** is a **traditional computer vision–based healthcare application** designed to verify whether a given tablet/pill image matches a known reference pill.  

The system aims to **reduce medication errors** by visually analyzing pill characteristics such as **shape, size, and color**, without using deep learning or large pretrained models.

This version represents the **Minimum Viable Product (MVP)** of the project and serves as the foundation for future upgrades such as **OCR-based prescription verification** and **database-driven user history tracking**.

---

## 🎯 Problem Statement

Medication errors due to:
- similar-looking pills,
- incorrect dispensing,
- and lack of visual verification tools

can cause serious health risks.

Most existing solutions rely on:
- manual checking, or
- heavy deep learning models requiring large datasets.

There is a need for a **lightweight, explainable, and low-resource solution** that can verify pills using **classical computer vision techniques**.

---

## 💡 Proposed Solution (v1)

PillCam-Lite v1.0 verifies pills using:
- **Image preprocessing**
- **Contour-based pill segmentation**
- **Feature extraction (shape, area, color)**
- **Feature similarity matching**

No deep learning or LLMs are used in this version.

---

## 🧠 Core Concepts Used

- Classical Computer Vision (OpenCV)
- Image Thresholding and Morphological Operations
- Contour Detection
- HSV Color Space Analysis
- Rule-based Feature Matching
- Flask Web Framework

---

## ⚙️ System Architecture (v1)

User → Web Interface → Image Upload
↓
Image Preprocessing
↓
Pill Segmentation
↓
Feature Extraction
(shape, area, color)
↓
Feature Matching
↓
Verification Result


---

## 🧪 Features Implemented (v1)

✔ Upload pill image  
✔ Segment pill from background  
✔ Extract visual features  
✔ Compare against reference dataset  
✔ Display verification result  
✔ Lightweight & fast execution  

---

## 🗂️ Project Structure

PillCam-Lite/
├── backend/
│ ├── app.py
│ ├── detect.py
│ ├── batch_register.py
│ └── requirements.txt
│
├── dataset/
│ ├── Paracetamol/
│ ├── VitaminC/
│ └── IronTablet/
│
├── static/
│ └── uploads/
│
├── templates/
│ ├── index.html
│ └── result.html
│
└── README.md


---

## 📊 Dataset

### Dataset Type
- **Reference image dataset**
- Class-wise pill images

### Dataset Characteristics
- Images captured on white background
- Top-down view of pills
- Synthetic dataset used for prototyping
- Easily replaceable with real pill images

---

## 🔍 Feature Extraction Details

| Feature | Description |
|------|------------|
| Shape | Determined using contour circularity |
| Area | Contour area in pixels |
| Color | Median HSV color values |
| Segmentation | Threshold + morphology |

---

## 🧮 Matching Strategy

- Euclidean distance–based similarity
- Color difference in HSV space
- Area difference thresholding
- Shape consistency check
- Final score aggregation across samples

---

## 🖥️ Installation & Setup

### Step 1: Clone Repository

git clone https://github.com/jhanani14/PillCam-Lite.git
cd PillCam-Lite

### Step 2: Create Virtual Environment

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

### Step 3: Install Dependencies

pip install -r backend/requirements.txt

### Step 4: Register Reference Pills

python backend/batch_register.py

### Step 5: Run Application

python backend/app.py

Open browser at:

http://127.0.0.1:5000
