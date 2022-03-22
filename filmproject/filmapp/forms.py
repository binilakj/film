from django import forms
from . models import Cinema

class Cinemaform(forms.ModelForm):
    class Meta:
        model=Cinema
        fields=['name','des','year','img']