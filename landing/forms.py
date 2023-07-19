from django import forms
from .models import *


class AuthorizationForm(forms.ModelForm):

    class Meta:
        model = Authorization
        exclude = [""]
