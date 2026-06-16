import streamlit as st
import cv2
import numpy as np
from PIL import Image
from preprocessing import preprocess_image
from ocr import extract_text
import pytesseract

# Set Tesseract path (IMPORTANT for Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("🧾 Handwritten Text Recognition App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert image to OpenCV format
    image = Image.open(uploaded_file)
    image = np.array(image)

    st.subheader("Original Image")
    st.image(image, use_column_width=True)

    # Preprocess
    processed = preprocess_image(image)

    st.subheader("Processed Image")
    st.image(processed, use_column_width=True)

    # OCR
    text = extract_text(processed)

    st.subheader("Extracted Text")
    st.write(text)