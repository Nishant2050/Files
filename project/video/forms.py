from django import forms
from .models import Document

class DocForm(forms.ModelForm):
    title = forms.CharField(max_length=120, required=True, help_text='max length = 120')

    class Meta:
        model = Document
        fields = ('title','docfile',)

