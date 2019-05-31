from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    emailAddress = forms.EmailField()
    message = forms.CharField()
