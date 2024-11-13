from django import forms
from django.core.mail import send_mail
class ContactForm(forms.Form):
    naam = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naam'}), label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}), label="")
    telefoonnummer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Telefoonnummer'}), label="")
    opmerkingen = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Opmerkingen'}), label="")

def send_email_task(subject, message, recipient_list, html_message=None):
    send_mail(subject, message, None, recipient_list, html_message=html_message)