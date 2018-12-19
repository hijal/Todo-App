from django import forms
from .models import List

class listForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']