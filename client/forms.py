from django import forms 

from .models import Client

class AddCLientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'description',)