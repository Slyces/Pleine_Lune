from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *


# Create your views here.
# @login_required
def home(request):
    user_list = User.objects.all()
    player=Player.objects.get(user=request.user)
    games_list = Game.objects.all().filter(player__exact=player)#Sélectionne la liste des parties ou le joueur connecté est impliqué
    return render(request, 'website/home.html', context={"user_list": user_list,"games_list": games_list,"player": player})


def current_game(request, game_id=0):
    form = ChampMessage(request.POST or None)
    user_list = User.objects.all()
    player = Player.objects.get(user=request.user)
    if form.is_valid():
        message = form.cleaned_data['message']
        #Message(content=message,sender=player,pub_date)
    else:
        message = "Tapez du texte !"
    print(message)
    return render(request, 'website/currentGame.html', context={"message": message,"id":game_id})


def game_list(request):
    return render(request, 'website/gameList.html')


def help_page(request):
    return render(request, 'website/help.html')


def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
            return HttpResponseRedirect('/thanks/')

            # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

