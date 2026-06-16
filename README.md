# 🧾 Handwritten Text Recognition using OCR

A deployable Handwritten Text Recognition (HTR) system built using Python, OpenCV, Tesseract OCR, and Streamlit. This project extracts text from handwritten images by applying image preprocessing techniques and Optical Character Recognition (OCR).

## 🚀 Features

- Upload handwritten images
- Image preprocessing using OpenCV
- Noise reduction and thresholding
- Text extraction using Tesseract OCR
- Simple and interactive Streamlit interface
- Real-time OCR results

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
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Handwritten-Text-Recognition.git
cd Handwritten-Text-Recognition
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Download and install Tesseract OCR:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the Tesseract path in `app.py`:

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
3. Apply noise reduction
4. Perform adaptive thresholding
5. Extract text using Tesseract OCR
6. Display recognized text

---

## 📸 Sample Output

Input:
- Handwritten image uploaded by user

Output:
- Preprocessed image
- Extracted digital text

---

## 🎯 Future Improvements

- Hindi Handwriting Recognition
- Multi-language OCR Support
- Download Extracted Text as TXT/PDF
- Improved Accuracy for Complex Handwriting
- Line and Word Segmentation

---

## 💡 Learning Outcomes

This project helped in understanding:

- Digital Image Processing (DIP)
- Image Preprocessing Techniques
- Optical Character Recognition (OCR)
- Streamlit Deployment
- Real-world Document Digitization

---

## 👨‍💻 Author

Developed as a Digital Image Processing (DIP) Project using OpenCV and OCR techniques.
