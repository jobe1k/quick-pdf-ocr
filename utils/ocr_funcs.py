from typing import Tuple, List, Optional  
from pdf2image import convert_from_bytes  
import pytesseract  
import re  
from concurrent.futures import ThreadPoolExecutor  
from PIL.Image import Image  
    
class PDFOCRProcessor:  
    """  
    A class to process PDF files and extract text using OCR (Optical Character Recognition).  
    """  
  
    def __init__(self, language: str = "eng", psm: int = 3, oem: int = 1) -> None:  
        """  
        Initialize the PDFOCRProcessor with the desired OCR language, page segmentation mode, and OCR engine mode.  
  
        Args:  
            language (str): The language code for OCR (e.g., 'eng' for English).  
            psm (int): Page segmentation mode (e.g., 3 for fully automatic page segmentation).  
            oem (int): OCR Engine mode (e.g., 1 for LSTM neural net only).  
        """  
        self.language: str = language  
        self.psm: int = psm  
        self.oem: int = oem  
        # Tesseract configuration string  
        self.tesseract_config: str = f"--psm {self.psm} --oem {self.oem}"  
  
    def clean_text(self, text: str) -> str:  
        """  
        Clean the OCR-extracted text by:  
        - Replacing multiple spaces with a single space.  
        - Replacing multiple newlines with a single newline.  
  
        Args:  
            text (str): The raw OCR-extracted text.  
  
        Returns:  
            str: The cleaned text.  
        """  
        # Replace multiple spaces with a single space  
        text = re.sub(r'\s{2,}', ' ', text)  
        # Replace multiple newlines with a single newline  
        text = re.sub(r'\n{2,}', '\n', text)  
        return text  
  
    def process_page(self, idx: int, pil_image: Image) -> str:  
        """  
        Perform OCR on a single page and clean the text.  
  
        Args:  
            idx (int): The page index (1-based).  
            pil_image (Image): The page image as a PIL Image object.  
  
        Returns:  
            str: The cleaned OCR text wrapped in <page_xx> tags.  
        """  
        # Perform OCR on the image  
        text = pytesseract.image_to_string(pil_image, lang=self.language, config=self.tesseract_config)  
        # Clean the extracted text  
        cleaned_text = self.clean_text(text)  
        # Wrap the cleaned text in <page_xx> tags  
        return f"<page_{idx}>\n{cleaned_text}\n</page_{idx}>"  
  
    def pdf_to_text(self, pdf_bytes: bytes, max_pages: Optional[int] = None, num_threads: int = 4) -> Tuple[List[str], int]:  
        """  
        Convert a PDF file (provided as bytes) into text using OCR.  
        Each page is processed in parallel, and the text is cleaned.  
  
        Args:  
            pdf_bytes (bytes): The binary content of the PDF file.  
            max_pages (Optional[int]): The maximum number of pages to process. If None, process all pages.  
            num_threads (int): The number of threads to use for parallel processing.  
  
        Returns:  
            Tuple[List[str], int]:  
                - A list of strings, where each string contains the OCR-processed text from a single page,  
                  wrapped in `<page_xx>` XML tags.  
                - The total number of pages processed.  
        """  
        # Convert the PDF bytes into a list of PIL images (one per page)  
        images = convert_from_bytes(pdf_bytes)  
  
        # Limit the number of pages to process if max_pages is specified  
        if max_pages is not None:  
            images = images[:max_pages]  
  
        all_text: List[str] = []  
  
        # Use a ThreadPoolExecutor to process pages in parallel  
        with ThreadPoolExecutor(max_workers=num_threads) as executor:  
            # Submit tasks for each page to the thread pool  
            results = [executor.submit(self.process_page, idx + 1, img) for idx, img in enumerate(images)]  
            # Collect the results as they complete  
            for future in results:  
                all_text.append(future.result())  
  
        # Return the processed text and the total number of pages  
        return all_text
