# Databricks notebook source
# MAGIC %md #### Install dependencies

# COMMAND ----------

# MAGIC %pip install pdf2image==1.17.0 pytesseract==0.3.10 PyMuPDF==1.25.3 -q
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %sh  
# MAGIC sudo apt update > /dev/null 2>&1  
# MAGIC sudo apt install -y poppler-utils > /dev/null 2>&1  

# COMMAND ----------

# MAGIC %md ##### Import modules and custom packages and run ocr

# COMMAND ----------

 if __name__ == '__main__':
     
    # Import necessary modules
    from utils.ocr_funcs import *
    from pathlib import Path 
    import time
    import gc
  
    # Create an instance of the PDFOCRProcessor  
    ocr_processor = PDFOCRProcessor(language="eng")  # Set OCR language to English  
    
    # Read the PDF file as bytes  
    pdf_path = Path("./test3.pdf")  # Path to  PDF file  
    with open(pdf_path, "rb") as pdf_file:  
        pdf_bytes = pdf_file.read()  
    
    # Start the timer  
    start_time = time.time()

    # Process the PDF using the class  
    texts, page_count = ocr_processor.pdf_to_text(pdf_bytes, max_pages=None)  

    # End the timer 
    end_time = time.time()  

    # Display the results  
    print(f"Total Pages: {page_count}\n")  
    for page_text in texts:  
        print(page_text)  

    # Elapsed time  
    elapsed_time = end_time - start_time  
    print(f"{'-'*100}\nTime taken: {elapsed_time:.2f} seconds")  

    # Delete reference and force garbage collection
    del pdf_bytes
    gc.collect()

# COMMAND ----------

