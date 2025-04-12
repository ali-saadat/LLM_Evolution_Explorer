"""
PDF document processing utilities for the LLM Evolution Explorer application.
"""
import os
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text from the PDF.
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"

def split_text(text, chunk_size=1000, chunk_overlap=200):
    """
    Split text into chunks for processing.
    
    Args:
        text (str): Text to split.
        chunk_size (int, optional): Size of each chunk. Defaults to 1000.
        chunk_overlap (int, optional): Overlap between chunks. Defaults to 200.
    
    Returns:
        list: List of text chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return text_splitter.split_text(text)

def save_uploaded_file(uploaded_file, directory):
    """
    Save an uploaded file to the specified directory.
    
    Args:
        uploaded_file: The uploaded file object from Streamlit.
        directory (str): Directory to save the file to.
    
    Returns:
        str: Path to the saved file.
    """
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path
