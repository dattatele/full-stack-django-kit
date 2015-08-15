from collections import OrderedDict
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(label=_('Email'))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # Again, investigate crispy forms for bootstrap friendly forms
        self.fields.pop('username')
        key_order = ['email', 'password1', 'password2']
        self.fields = OrderedDict((k, self.fields[k]) for k in key_order)
        self.fields['email'].widget.attrs["class"] = 'form-control'
        self.fields['password1'].widget.attrs["class"] = 'form-control'
        self.fields['password2'].widget.attrs["class"] = 'form-control'

