import os
from datetime import datetime

UPLOAD_FOLDER = "uploads"

def save_pdf(file):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    with open(os.path.join(UPLOAD_FOLDER, filename), "wb") as f:
        f.write(file.file.read())
    return "saved"
