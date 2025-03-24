import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path

# Set the path for Tesseract OCR (update this path if needed)
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"  # Change this for your OS

def extract_highlighted_text(pdf_path, output_txt_path):
    images = convert_from_path(pdf_path)  # Convert PDF pages to images
    extracted_texts = []

    for img in images:
        # Convert image to OpenCV format
        img = np.array(img)
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        # Define the range for detecting the highlight color (PINK example)
        lower_pink = np.array([140, 50, 50])  # Adjust these values if needed
        upper_pink = np.array([180, 255, 255])
        
        mask = cv2.inRange(hsv, lower_pink, upper_pink)  # Create a mask for pink highlights
        mask = cv2.dilate(mask, None, iterations=2)  # Expand the mask slightly

        # Find contours of highlighted areas
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            highlighted_region = img[y:y+h, x:x+w]  # Crop highlighted text region
            
            # Extract text using Tesseract OCR
            text = pytesseract.image_to_string(highlighted_region, lang="eng").strip()
            if text:
                extracted_texts.append(text)

    # Save extracted text to a file
    if extracted_texts:
        with open(output_txt_path, "w", encoding="utf-8") as f:
            for text in extracted_texts:
                f.write(text + "\n\n")
        print(f"Extracted highlights saved to {output_txt_path}")
    else:
        print("No highlights detected! Try adjusting the color range.")

# Example usage
extract_highlighted_text("FGV-DAPP-2020-A-economia-de-Roraima-e-o-fluxo-vene_250323_141023.pdf", "highlights.txt")
