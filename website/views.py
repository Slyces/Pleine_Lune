from django.shortcuts import render
from django.views import View


# Create your views here.
def home(request):
    return render(request, 'website/home.html')


def current_game(request):
    return render(request, 'website/currentGame.html')


def game_list(request):
    return render(request, 'website/gameList.html')


def help_page(request):
    return render(request, 'website/help.html')


def register(request):
    return render(request, 'registration/register.html')


class Login(View):
    pass
