from django.db import models
from .views import User


# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=50, blank=True)
    game = models.ManyToManyField(Game)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    # @TODO Etat dans le jeu (mort, Cupidon...)
    # @TODO Droits (chans visibles)
    # @TODO profile picture


class Role(models.Model):
    name = models.TextField(max_length=50, blank=True)
    description = models.TextField(max_length=500, blank=True)
    officiel = models.BooleanField(blank=True)
    # @TODO profile picture


class Game(models.Model):
    name = models.TextField(max_length=50, blank=True)
    gamemode = models.TextField(max_length=50, blank=True)
    players = models.ManyToManyField(Player)
    # @TODO Etat du jeu

class Message(models.Model):
    content = models.TextField(max_length=500, blank=True)
    sender = models.ForeignKey(Player, on_delete=models.CASCADE)
    pub_date = models.DateField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # @TODO tag du message