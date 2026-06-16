# 🧾 Handwritten Text Recognition using OCR

A Digital Image Processing (DIP) project that converts handwritten text images into machine-readable text using image preprocessing techniques and Optical Character Recognition (OCR).

## 🚀 Features

- Upload handwritten images
- Image preprocessing using OpenCV
- Noise reduction and adaptive thresholding
- Text extraction using Tesseract OCR
- Interactive Streamlit web interface
- Real-time OCR output

---

## 🛠️ Technologies Used

- Python
- OpenCV
- Tesseract OCR
- Pytesseract
- Streamlit
- NumPy
- Pillow

---

## 📂 Project Structure

```text
HTR-Project/
│
├── app.py
├── preprocessing.py
├── ocr.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── Original image.png
    └── Processed image.png
```

---

## ⚙️ Installation

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Tesseract OCR

Download and install Tesseract OCR:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the path in `app.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

1. Upload a handwritten image
2. Convert image to grayscale
3. Apply Gaussian Blur for noise reduction
4. Perform Adaptive Thresholding
5. Extract text using Tesseract OCR
6. Display the recognized text

---

## 📸 Screenshots

### Original Image

![Original Image](screenshots/Original%20Image.png)

### Processed Image

![Processed Image](screenshots/Processed%20Image.png)

---

## 🎯 Future Enhancements

- Hindi Handwriting Recognition
- Multi-language OCR Support
- Export OCR results to PDF/TXT
- Improved recognition for complex handwriting
- Word and line segmentation

---

## 📚 Learning Outcomes

Through this project, I learned:

- Digital Image Processing fundamentals
- Image preprocessing techniques
- Optical Character Recognition (OCR)
- OpenCV integration with Python
- Streamlit application development
- Deploying practical DIP solutions

---

## 👨‍💻 Author

Developed as a Digital Image Processing (DIP) Project using OpenCV, Tesseract OCR, and Streamlit.
