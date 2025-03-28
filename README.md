# PDFOCRProcessor

`PDFOCRProcessor` is a Python class designed to process PDF files and extract text using **OCR (Optical Character Recognition)**. It is particularly useful for working with scanned or image-based PDFs where text extraction requires OCR.

---

## Features

- **OCR for PDFs**: Converts PDFs (including scanned/image-based ones) to text using **Tesseract OCR**.
- **Customizable Settings**:
    - Language support (e.g., `eng` for English, `fra` for French).
    - Page segmentation mode (PSM) and OCR engine mode (OEM).
- **Parallel Processing**: Processes multiple pages simultaneously using multithreading for faster results.
- **Text Cleaning**: Cleans extracted text by removing unnecessary spaces and line breaks.
- **Structured Output**: Wraps text in `<page_xx>` tags for easy parsing.

---

## Installation

### 1. Install Python Libraries

Run the following command to install the required Python libraries:

```bash
pip install pdf2image==1.17.0 pytesseract==0.3.10 PyMuPDF==1.25.3
```

### 2. Install System Dependencies

**Poppler**: Required by `pdf2image` to convert PDF pages to images.
**Tesseract OCR**: Required for performing OCR on images.

**For Ubuntu/Debian systems:**

```bash
sudo apt update
sudo apt install -y poppler-utils tesseract-ocr
```

**For MacOS (via Homebrew):**

```bash
brew install poppler tesseract
```

**For Windows:**

Download and install [Poppler](https://github.com/oschwartz10611/poppler-windows/releases).
Download and install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki).

---

## Usage

### Import and Initialize

First, import the class and initialize it with your desired OCR settings:

```python
from pdf_ocr_processor import PDFOCRProcessor

# Initialize the OCR processor with default settings
processor = PDFOCRProcessor(language="eng", psm=3, oem=1)
```

### Convert PDF to Text

To process a PDF file, provide the PDF as a binary (bytes) object. The `pdf_to_text` method will return:

- A list of strings (one for each page) with OCR-processed and cleaned text.
- The total number of pages processed.

**Example:**

```python
# Read the PDF as binary data
with open("scanned_document.pdf", "rb") as f:
    pdf_bytes = f.read()

# Convert the PDF to text
text, page_count = processor.pdf_to_text(pdf_bytes, max_pages=None, num_threads=4)

# Print the results
print(f"Processed {page_count} pages!")
for page_text in text:
    print(page_text)
```

---

## Example Output

For a 2-page scanned PDF, the output might look like this:

```
Processed 2 pages!
<page_1>
This is the text extracted from page 1.
</page_1>
<page_2>
This is the text extracted from page 2.
</page_2>
```
```
