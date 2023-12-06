from django import forms
from .models import product

class productfrom(forms.ModelForm):
    class Meta:
        model=product
        fields=['name','desc','price','stock','img']

