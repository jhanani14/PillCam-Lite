import cv2
import numpy as np
import os

def match_pill(image_path):
    # Simple color + contour logic (traditional CV)
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    if np.sum(edges) > 10000:
        return "Paracetamol"
    return "Unknown"
