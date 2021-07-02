from django import forms
from .models import Furniture

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture

        fields = ('__all__')
  