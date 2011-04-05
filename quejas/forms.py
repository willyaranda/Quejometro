from django import forms
from django.forms import ModelForm
from quejas.models import Queja

class QuejaForm(ModelForm):
    class Meta:
        model = Queja