from django import forms
from .models import Dr_info

class Dr_form(forms.ModelForm):
    class Meta:
        model = Dr_info
        fields = ('Dr_photo_link',)
class FileUploadForm(forms.Form):
    file_source = forms.FileField()