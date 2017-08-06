from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from django.http import JsonResponse


# Create your views here.
@login_required
def home(request):
    user_list = User.objects.all()
    player=Player.objects.get(user=request.user)
    games_list = Game.objects.all().filter(player__exact=player)#Sélectionne la liste des parties ou le joueur connecté est impliqué
    return render(request, 'website/home.html', context={"user_list": user_list,"games_list": games_list,"player": player})


def current_game(request, game_id=0):
    form = ChampMessage(request.POST or None)#recupération des données
    player = Player.objects.get(user=request.user)
    game = Game.objects.get(id=game_id)
    player_list=game.player.all()
    nom_du_village=game.name

    if form.is_valid() and "id_form" in request.POST and request.POST["id_form"]=="1":
        message = form.cleaned_data['message']#Ajout du messages à la BDD
        Message(content=message, sender=player, pub_date=datetime.datetime.now(), game=game).save()
    elif "id_form" in request.POST and request.POST["id_form"]=="2":
        message = "Tapez du texte !"
        game.player.add(player)
        Message(content="Un joueur a rejoint la partie !", sender=player, pub_date=datetime.datetime.now(), game=game).save()
    else:
        message = "Tapez du texte !"

    chat = Message.objects.filter(game__exact=game).order_by('pub_date')  # Tri des messages (après avoir potentiellement update la BDD)
    player_in_village = player in player_list  # True si le joueur participe à cette partie

    chat = Message.objects.all().order_by('pub_date')  # Tri des messages (après avoir potentiellement update la BDD)
    chat = chat[max(len(chat) - 20, 0):len(chat)]  # Chargement des 20 derniers messages
    return render(request, 'website/currentGame.html', context={"message": message,"chat":chat,"player_list":player_list,"nom_du_village":nom_du_village,"player_in_village":player_in_village})


def game_list(request):
    games_being_created=Game.objects.filter(started__exact=False)
    games_started=Game.objects.filter(started__exact=True)
    return render(request, 'website/gameList.html',context={'gamesStarted':games_started,'gamesBeingCreated':games_being_created})
    #return render(request, 'website/gameList.html')


def help_page(request):
    return render(request, 'website/help.html')


def create_game(request):
    if request.method == 'POST':
        form=CreateGameForm(request.POST)
        if form.is_valid():
            player = Player.objects.get(user=request.user)
            id_game=Game.objects.all().count()+1
            g=Game(id=id_game,name=form.cleaned_data['game_name'],gamemode=form.cleaned_data['gamemode'],started=False)
            g.save()
            g.player.add(player)
            # @TODO Aménager une page po
            # ur les parties en attente de joueurs
            return HttpResponseRedirect(reverse('home'))
    else:
        form = CreateGameForm()
    return render(request, 'website/createGame.html',{'form':form})


def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
            return HttpResponseRedirect(reverse('home'))

            # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)