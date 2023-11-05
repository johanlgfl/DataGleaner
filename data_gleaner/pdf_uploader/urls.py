# Django imports
from django.urls import path

# Project imports
from pdf_uploader import views

app_name = 'pdf_uploader'

# Create your urls here.
urlpatterns = [
    path('upload/', views.UploadPDFView.as_view(), name='upload_pdf'),
]