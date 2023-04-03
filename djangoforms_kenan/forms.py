from django import forms


class Contact_form(forms.Form):
    name = forms.CharField(max_length=100, help_text="Enter YOUR name")
    email = forms.EmailField(help_text='Enter your email')
    file=forms.FileField()
    message = forms.CharField(widget=forms.Textarea, help_text='Enter your message')

