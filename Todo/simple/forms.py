from django import forms
from .models import Newdata

class Newform(forms.ModelForm):
    class Meta():
        model=Newdata
        fields='__all__'
