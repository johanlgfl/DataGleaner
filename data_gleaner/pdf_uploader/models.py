# Django imports
from django.db import models

# Project imports
from pdf_uploader import utils


# Create your models here.
class PDFDocument(models.Model):
    """
    Models for storing PDF documents uploaded by users.

    Attributes:
        document (FileField): FileField for storing the PDF document.
        uploaded_by (ForeignKey): User who uploaded the file.
        uploaded_date (DateTimeField): Date and time the file was uploaded.
    """
    document = models.FileField(upload_to=utils.pdf_directory_path)
    uploaded_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    uploaded_date = models.DateTimeField(auto_now_add=True)