from django import forms
from .models import Services
from django import forms

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

