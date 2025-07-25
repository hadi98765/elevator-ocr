from PIL import Image
import pytesseract
import io

def process_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes))
    text = pytesseract.image_to_string(image, lang="eng+fas")
    return text.strip()
