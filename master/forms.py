from django.forms import inlineformset_factory

from django import forms
from .models import StoreDetail

class StoreDetailForm(forms.ModelForm):
    class Meta:
        model = StoreDetail
        fields = '__all__'
