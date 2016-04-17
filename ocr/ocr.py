import pytesseract
from PIL import Image


def ocr(image_path):
    return pytesseract.image_to_string(Image.open(image_path))
