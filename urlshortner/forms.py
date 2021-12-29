from django import forms

class LinkForm(forms.Form):
    long_url = forms.URLField(label='URL to shorten', max_length=250)