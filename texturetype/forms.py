from django import forms
from .models import TextureType

class TextureTypeForm(forms.ModelForm):
    class Meta:
        model = TextureType

        fields = ('__all__')
  