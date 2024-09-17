from django import forms
from .models import Contacts_manage

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts_manage
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']