Here's a complete `README.md` file for your project. I'll include project details, setup instructions, dependencies, usage, and more.

### `README.md`
Here's a complete `README.md` file for your ML invoice extraction project:

---

```markdown
# Invoice Extraction using Tesseract and Spacy

This project is an invoice extraction system using **Python**, **Tesseract** for OCR, and **Spacy** for Named Entity Recognition (NER). It extracts key details like invoice number, date, and line items from invoice images.

---

## 🚀 **Project Overview**
The goal of this project is to:
- Extract invoice number, invoice date, and line items from invoice images.
- Build a scalable model that allows training for any field extraction.
- Use OCR to convert PDF invoices to images.
- Train a Spacy model to recognize key-value pairs from extracted text.

---

## 📂 **Project Structure**
```
📦 masterindia
├── 📁 output
│   ├── invoice_1.png
│   └── spacy_invoice_model
├── 📁 data
│   └── sample.pdf
├── 📁 model
│   ├── config.cfg
├── app.py
├── requirements.txt
├── train.py
├── README.md
└── .gitignore
```

---

## 🛠️ **Setup Instructions**
### 1. **Clone the Repository**
```bash
git clone https://github.com/WhozKunal/Assignment-for-ML-Mastersindia.git
cd Assignment-for-ML-Mastersindia
```

---

### 2. **Create Virtual Environment**
```bash
python -m venv venv
```

---

### 3. **Activate Virtual Environment**
- **Windows**:
```bash
.\venv\Scripts\activate
```
- **Linux/Mac**:
```bash
source venv/bin/activate
```

---

### 4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

### 5. **Install Poppler**
- Download Poppler from [https://github.com/oschwartz10612/poppler-windows/releases/](https://github.com/oschwartz10612/poppler-windows/releases/)
- Extract it and add the `bin` folder to the **PATH**:
    - **Windows**:
        1. Go to **System Properties → Advanced → Environment Variables**
        2. Add `C:\path-to-poppler\bin` to the `PATH` variable.

---

### 6. **Set Up Tesseract**
- Download Tesseract from [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract).
- Add the installation path to the **PATH**:
    - Example:
    ```
    C:\Program Files\Tesseract-OCR
    ```
- Verify Installation:
```bash
tesseract -v
```

---

### 7. **Train Spacy Model**
- Create a Spacy configuration file:
```bash
python -m spacy init config model/config.cfg --lang en --pipeline ner
```
- Train the model:
```bash
python train.py
```

---

## 💻 **Usage**
### 1. **Run the Application**
```bash
python app.py
```

### 2. **Output Example**
```
Converting PDF to images...
Extracting text from output/invoice_1.png...
Extracted text:
INVOICE DATE: 01/01/1970
INVOICE NUMBER: 001
...
Training Spacy model...
Prediction result:
{'INVOICE_NUMBER': '001', 'INVOICE_DATE': '01/01/1970'}
```

---

## ✅ **Sample Output**
Example of extracted fields:
| Field            | Value             |
|------------------|-------------------|
| INVOICE NUMBER    | 001               |
| INVOICE DATE      | 01/01/1970        |
| CUSTOMER NAME     | John Doe          |
| LINE ITEMS        | Item 1, Item 2    |

---

## 📖 **Model Details**
- **OCR Tool**: Tesseract
- **NER Model**: Spacy
- **Training Loss**:
    - Iteration 1: `{'ner': np.float32(129.60)}`
    - Iteration 100: `{'ner': np.float32(7.35e-09)}`
- **Text Processing**:
    - Cleaning
    - Tokenization
    - Entity extraction

---

## ⚠️ **Troubleshooting**
### 1. `FileNotFoundError: [WinError 2]`  
➡️ Make sure Poppler and Tesseract are installed and added to the PATH.

### 2. `PDFInfoNotInstalledError`  
➡️ Ensure that Poppler is correctly installed and accessible from the command line.

### 3. `Unexpected type for NER data`  
➡️ Verify the annotations format in the Spacy training data.

---

## 🏆 **Contributing**
If you want to improve this project:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make changes and test
4. Commit changes (`git commit -m "Feature: added support for xyz"`)
5. Push (`git push origin feature-branch`)
6. Create a Pull Request

---

## 📄 **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 **Author**
- **Kunal Kumar Singh**  
[GitHub](https://github.com/WhozKunal) | [LinkedIn](https://linkedin.com/in/kunalkumar9616)  

---

```

---

### ✅ **Steps to Add to GitHub**
1. Add the file:
```bash
git add README.md
```
2. Commit the file:
```bash
git commit -m "Added README.md"
```
3. Push the file:
```bash
git push origin main
```

---

Let me know if you want to add or modify anything! 😎
