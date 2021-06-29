from django import forms
from .models import HomeType

class HomeTypeForm(forms.ModelForm):
    class Meta:
        model = HomeType

        fields = ('__all__')
  