from django.contrib.auth.models import User
from django.contrib.auth import forms as auth_forms
# from django.contrib.auth.models import User
from django.contrib.auth import forms
from django import forms


class ChampMessage(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class RegisterForm(forms.Form):
    username = auth_forms.UsernameField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

class CreateGameForm(forms.Form):
    game_name = forms.CharField(max_length=50)
    gamemode = forms.CharField(max_length=50)

class JoinGame(forms.Form):
    pass