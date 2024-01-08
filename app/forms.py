from django import forms

from app.models import *

class Data1(forms.ModelForm):
    class Meta:
        model=Data
        fields='__all__'

class Web(forms.ModelForm):
    class Meta:
        model=Web
        fields='__all__'