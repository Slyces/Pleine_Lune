from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/?', views.home, name='home'),
    url(r'^currentGame/?', views.currentGame, name='currentGame'),
    url(r'^gameList/?', views.gameList, name='gameList'),
    url(r'^help/?', views.help, name='help'),
]
