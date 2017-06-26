# hanlde customized forms
from django import forms

# fields from form class map to HTML elements.
class TinyurlForm(forms.Form):
    long_url = forms.CharField(max_length=100)
    #short_url = forms.CharField(max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    # we can use a password input widget so the characters are hidden
    password = forms.CharField(widget = forms.PasswordInput())


