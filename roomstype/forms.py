from django import forms
from .models import RoomsType

class RoomsTypeForm(forms.ModelForm):
    class Meta:
        model = RoomsType

        fields = ('__all__')
  