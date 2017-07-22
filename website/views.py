from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def currentGame(request):
    return render(request, 'website/currentGame.html')

def gameList(request):
    return render(request, 'website/gameList.html')

def help(request):
    return render(request, 'website/help.html')
