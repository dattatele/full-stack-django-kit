from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Customer


class CustomerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs["class"] = 'form-control'

    class Meta:
        model = Customer
        fields = ['name']
        labels = {
            'name': _('Name'),
        }
