import cv2
import pytesseract
from config import settings

pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_CMD

def image_to_text(image_path):
    img = cv2.imread(str(image_path))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='eng+rus')
    return text.strip()