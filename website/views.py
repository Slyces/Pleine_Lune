from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    user_list = User.objects.all()
    return render(request, 'website/home.html', context={"user_list": user_list})

def currentGame(request):
    return render(request, 'website/currentGame.html')

def gameList(request):
    return render(request, 'website/gameList.html')

def help(request):
    return render(request, 'website/help.html')
