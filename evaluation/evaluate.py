import os
import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

from cv.matcher import match_pill

# ---------------- PATHS ---------------- #
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_DIR = os.path.join(BASE_DIR, "data", "raw", "images")
REF_DB = os.path.join(BASE_DIR, "data", "reference_db", "features.pkl")
OUT_DIR = os.path.join(BASE_DIR, "evaluation")

os.makedirs(OUT_DIR, exist_ok=True)

# ---------------- DATA COLLECTION ---------------- #
y_true = []
y_pred = []

print("[INFO] Starting evaluation...")

for img_name in os.listdir(TEST_DIR):
    if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    img_path = os.path.join(TEST_DIR, img_name)

    # Naming convention: pillname_1.jpg
    true_label = img_name.split("_")[0]
    predicted_label = match_pill(img_path)

    y_true.append(true_label)
    y_pred.append(predicted_label)

# ---------------- METRICS ---------------- #
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average="weighted", zero_division=0)
recall = recall_score(y_true, y_pred, average="weighted", zero_division=0)

print("\n===== EVALUATION RESULTS =====")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")

# ---------------- CONFUSION MATRIX ---------------- #
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(8, 6))
plt.imshow(cm, interpolation="nearest")
plt.title("Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()

cm_path = os.path.join(OUT_DIR, "confusion_matrix.png")
plt.savefig(cm_path)
plt.close()

print(f"\n[✓] Confusion matrix saved to {cm_path}")
print("[✓] Evaluation completed successfully")
