# coding=utf-8
from django import forms
from django.forms import ModelForm
from claims.models import Claim

class ClaimForm(ModelForm):
    class Meta:
        model = Claim