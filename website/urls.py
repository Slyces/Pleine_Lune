from django.conf.urls import url
import django.contrib.auth.views as auth_views
from . import views

urlpatterns = [
    url(r'^home/?$', views.home, name='home'),
    url(r'^accounts/login/?$', views.login_view, name='login'),
    url(r'^accounts/logout/?$', auth_views.logout, name='logout'),
    url(r'^currentGame/?', views.current_game, name='currentGame'),
    url(r'^gameList/?', views.game_list, name='gameList'),
    url(r'^help/?', views.help_page, name='help'),
    url(r'^accounts/register', views.register, name='register'),
]
