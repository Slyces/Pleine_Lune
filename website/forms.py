from django.contrib.auth.models import User
from django.contrib.auth import forms
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class champMessage(forms.Form):
    message = forms.CharField(widget=forms.Textarea)