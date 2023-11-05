# Django imports
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

# Project imports
from pdf_uploader import forms
from pdf_uploader import models


# Create your views here.
class UploadPDFView(FormView):
    """
    View for uploading PDFs.
    """
    template_name = 'pdf_uploader/upload_pdf.html'
    form_class = forms.UploadPDFForm

    def form_valid(self, form):
        """
        Method that runs if the form is valid.
        Performs PDF file processing logic.

        Args:
            form (UploadPDFForm): Form to validate.
        """
        file_field = form.cleaned_data['file_field']
        usuario = self.request.user

        for file in file_field:
            pdf_document = models.PDFDocument(
                document=file,
                uploaded_by=usuario
            )
            pdf_document.save()

        return super().form_valid(form)

    def get_success_url(self):
        """
        Method to get the URL to redirect to after a successful form submission.
        """
        return reverse_lazy('pdf_uploader:upload_pdf')