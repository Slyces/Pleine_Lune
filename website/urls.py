from django.conf.urls import url
import django.contrib.auth.views as auth_views
from . import views

urlpatterns = [
    url(r'^home/?$', views.home, name='home'),
    # url(r'^accounts/login/?$', auth_views.login, name='login'),
    # url(r'^accounts/logout/?$', auth_views.logout, name='logout'),
    url(r'^currentGame/(?P<game_id>[0-9]*)/?$', views.current_game, name='currentGame'),
    url(r'^gameList/?', views.game_list, name='gameList'),
    url(r'^help/?', views.help_page, name='help'),
    url(r'^createGame/', views.create_game, name='createGame'),
]
