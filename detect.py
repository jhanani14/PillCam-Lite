import cv2
import numpy as np
import json
import os

DB_FILE = "pills_database.json"

# Function to extract features from an image
def extract_features(img_path):
    img = cv2.imread(img_path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mean_color = cv2.mean(img_hsv)[:3]  # HSV mean
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area = cv2.contourArea(contours[0]) if contours else 0
    return {"mean_h": mean_color[0], "mean_s": mean_color[1], "mean_v": mean_color[2], "area": area}

# Compare two feature dicts
def compare_features(f1, f2):
    color_diff = abs(f1['mean_h']-f2['mean_h']) + abs(f1['mean_s']-f2['mean_s']) + abs(f1['mean_v']-f2['mean_v'])
    area_diff = abs(f1['area'] - f2['area'])
    score = color_diff + area_diff/1000  # simple scoring
    return score

# Load database
def load_database():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, 'r') as f:
        return json.load(f)

# Find best match
def find_best_match(img_path):
    features = extract_features(img_path)
    db = load_database()
    best_match = None
    best_score = float('inf')
    for pill_name, pill_features_list in db.items():
        for f in pill_features_list:
            score = compare_features(features, f)
            if score < best_score:
                best_score = score
                best_match = pill_name
    return best_match, best_score
