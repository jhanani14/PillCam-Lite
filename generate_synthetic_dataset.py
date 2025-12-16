import cv2
import numpy as np
import os

dataset_dir = "dataset"
test_dir = "test_dataset"

pill_classes = {
    "Paracetamol": {"color": (255, 255, 255), "shape": "circle"},
    "VitaminC": {"color": (0, 165, 255), "shape": "circle"},
    "IronTablet": {"color": (0, 0, 255), "shape": "oval"}
}

num_train = 5
num_test = 3

for dir_path in [dataset_dir, test_dir]:
    for pill_name in pill_classes.keys():
        os.makedirs(os.path.join(dir_path, pill_name), exist_ok=True)

def draw_pill(shape, color):
    img = np.ones((200, 200, 3), dtype=np.uint8) * 255
    if shape == "circle":
        cv2.circle(img, (100, 100), 50, color, -1)
    elif shape == "oval":
        cv2.ellipse(img, (100, 100), (60, 40), 0, 0, 360, color, -1)
    return img

# Train images
for pill_name, info in pill_classes.items():
    for i in range(num_train):
        img = draw_pill(info["shape"], info["color"])
        noise = np.random.randint(0, 20, (200, 200, 3), dtype=np.uint8)
        img = cv2.add(img, noise)
        cv2.imwrite(f"{dataset_dir}/{pill_name}/img{i+1}.png", img)

# Test images
for pill_name, info in pill_classes.items():
    for i in range(num_test):
        img = draw_pill(info["shape"], info["color"])
        noise = np.random.randint(0, 30, (200, 200, 3), dtype=np.uint8)
        img = cv2.add(img, noise)
        cv2.imwrite(f"{test_dir}/{pill_name}/img{i+1}.png", img)

print("Synthetic dataset generated successfully!")
