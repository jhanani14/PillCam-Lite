import pytesseract
import cv2
import config

pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_CMD

def extract_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()
