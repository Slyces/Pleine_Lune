from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required
def home(request):
    user_list = User.objects.all()
    return render(request, 'website/home.html', context={"user_list": user_list})


def current_game(request):
    return render(request, 'website/currentGame.html')


def game_list(request):
    return render(request, 'website/gameList.html')


def help_page(request):
    return render(request, 'website/help.html')


def register(request):
    return render(request, 'registration/register.html')
