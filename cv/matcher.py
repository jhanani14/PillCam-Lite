import os
import pickle
import numpy as np

from cv.feature_extractor import extract_features

# ---------------- PATH ---------------- #
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FEATURE_DB_PATH = os.path.join(BASE_DIR, "data", "reference_db", "features.pkl")


def match_pill(image_path):
    """
    Matches uploaded pill image with reference database
    Returns best matched pill (image name)
    """

    # 1️⃣ Check reference DB
    if not os.path.exists(FEATURE_DB_PATH):
        return "Reference DB not found"

    # 2️⃣ Load reference features
    with open(FEATURE_DB_PATH, "rb") as f:
        reference_db = pickle.load(f)

    # 3️⃣ Extract features from uploaded image (PASS PATH ✔)
    query_features = extract_features(image_path)

    if query_features is None:
        return "Invalid image"

    best_match = None
    best_score = float("inf")

    # 4️⃣ Compare with reference features
    for name, ref_features in reference_db.items():
        if ref_features is None:
            continue

        distance = np.linalg.norm(query_features - ref_features)

        if distance < best_score:
            best_score = distance
            best_match = name

    # 5️⃣ Result
    return best_match if best_match else "No match found"
