from django import forms
from .models import Branch

class BrachForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['username', 'branch', 'c1', 'c2','c3','c4','c5','c6','c7']