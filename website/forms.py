# from django.contrib.auth.models import User
from django.contrib.auth import forms
from django import forms

class ChampMessage(forms.Form):
    message = forms.CharField(widget=forms.Textarea)