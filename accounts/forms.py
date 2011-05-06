# coding=utf-8
from django import forms
from django.forms import ModelForm
from accounts.models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile