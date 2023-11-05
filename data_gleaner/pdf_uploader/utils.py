# Python imports
from datetime import datetime


def pdf_directory_path(instance, filename):
    """
    Function to return the path to the PDF file.

    Args:
        instance (PDFDocument): Instance of the PDFDocument model.
        filename (str): Name of the file.

    Returns:
        str: Path to the PDF file.
    """
    now = datetime.now()
    return f'documents/pdf/{now.year}/{now.month}/{filename}'