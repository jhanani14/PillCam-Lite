import cv2
import numpy as np
from .preprocess import preprocess_image

def extract_features(path):
    img = preprocess_image(path)

    # SAFETY CHECK
    if img is None:
        print(f"[ERROR] Cannot read image: {path}")
        return np.zeros((32,), dtype=np.float32)

    orb = cv2.ORB_create(nfeatures=500)
    kp, des = orb.detectAndCompute(img, None)

    if des is None:
        return np.zeros((32,), dtype=np.float32)

    return des.mean(axis=0)
