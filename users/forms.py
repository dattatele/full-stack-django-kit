from collections import OrderedDict
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # Again, investigate crispy forms for bootstrap friendly forms
        key_order = ['username', 'email', 'password1', 'password2']
        self.fields = OrderedDict((k, self.fields[k]) for k in key_order)
        self.fields['username'].widget.attrs["class"] = 'form-control'
        self.fields['email'].widget.attrs["class"] = 'form-control'
        self.fields['password1'].widget.attrs["class"] = 'form-control'
        self.fields['password2'].widget.attrs["class"] = 'form-control'


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = 'form-control'
        self.fields['password'].widget.attrs["class"] = 'form-control'
