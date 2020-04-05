from django import forms
from main.models import path

class shorten(forms.ModelForm):
    
    class Meta:
        model = path
        fields = ('url',)