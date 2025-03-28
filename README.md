# PDFOCRProcessor  
  
A Python class to process PDF files and extract text using OCR (Optical Character Recognition). This is particularly useful for working with scanned or image-based PDFs where text extraction requires OCR.  
  
---  
  
## Features  
  
- Converts PDFs (including scanned/image-based ones) to text using **Tesseract OCR**.  
- Supports **customizable OCR settings**:  
  - Language (`eng`, `fra`, etc.).  
  - Page segmentation mode (PSM).  
  - OCR engine mode (OEM).  
- Processes multiple pages **in parallel** for faster performance.  
- Cleans up extracted text by removing unnecessary spaces and line breaks.  
- Outputs text wrapped in `<page_xx>` tags for easy parsing.  
  
---  
  
## Installation  
  
Before using the class, you need to install the required dependencies and tools.  
  
### 1. Install Python Libraries  
Run the following command to install the necessary Python libraries:  
```bash  
pip install pdf2image==1.17.0 pytesseract==0.3.10 PyMuPDF==1.25.3  
