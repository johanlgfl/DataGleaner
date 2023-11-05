# Django imports
from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    """
    A multiple-file version of Django's ClearableFileInput.
    """
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    """
    A multiple-file version of Django's FileField.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


# Create your forms here.
class UploadPDFForm(forms.Form):
    """
    Form for uploading PDFs.

    Attributes:
        pdf_file (FileField): PDF file to upload.
    """
    file_field = MultipleFileField(
        label='Seleccione uno o varios archivos PDF',
        required=True
    )

    def clean_file_field(self):
        """
        Clean the file field, checking that the files are PDFs.
        """
        data = self.cleaned_data['file_field']
        for file in data:
            if file.content_type != 'application/pdf':
                raise forms.ValidationError(
                    'El archivo {} no es un PDF.'.format(file.name)
                )

        return data