from django.conf.urls import url
import django.contrib.auth.views as auth_views
from . import views

urlpatterns = [
    url(r'^home/?$', views.home, name='home'),
    url(r'^login/?$', auth_views.login, name='login'),
    url(r'^logout/?$', auth_views.logout, name='logout'),
    url(r'^currentGame/?', views.currentGame, name='currentGame'),
    url(r'^gameList/?', views.gameList, name='gameList'),
    url(r'^help/?', views.help, name='help'),
]
