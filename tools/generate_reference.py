import os
import pickle
from cv.feature_extractor import extract_features

RAW_DIR = "data/raw/images"
OUT_FILE = "data/reference_db/features.pkl"

features = {}

for img in os.listdir(RAW_DIR):
    path = os.path.join(RAW_DIR, img)
    features[img] = extract_features(path)

os.makedirs("data/reference_db", exist_ok=True)

with open(OUT_FILE, "wb") as f:
    pickle.dump(features, f)

print("✅ Reference features saved to", OUT_FILE)
