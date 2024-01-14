from django import forms
from .models import SellBook1


class SellBookForm(forms.ModelForm):
    class Meta:
        model = SellBook1
        fields = '__all__'
