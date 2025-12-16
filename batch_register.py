import os
import json
from detect import extract_features, DB_FILE

DATASET_DIR = "dataset"

database = {}

for pill_name in os.listdir(DATASET_DIR):
    pill_folder = os.path.join(DATASET_DIR, pill_name)
    if os.path.isdir(pill_folder):
        features_list = []
        for img_file in os.listdir(pill_folder):
            img_path = os.path.join(pill_folder, img_file)
            features = extract_features(img_path)
            features_list.append(features)
        database[pill_name] = features_list

with open(DB_FILE, 'w') as f:
    json.dump(database, f, indent=4)

print("Pill database created successfully!")
