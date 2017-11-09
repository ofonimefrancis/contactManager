from django import forms
from .models import Contact

class ContactsForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'fields': '', 'class': "form-control", 'id': 'name', 'placeholder': 'Enter Full Name'}),
            'email': forms.EmailInput(attrs={'class': "form-control", 'id': 'email', 'placeholder': 'Enter E-mail address'}),
        }