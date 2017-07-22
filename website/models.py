from django.db import models
from .views import User


# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=50, blank=True)
    # profile picture
    # game
    # Role


class Role(models.Model):
    name = models.TextField(max_length=50, blank=True)
    description = models.TextField(max_length=50, blank=True)
    origin = models.TextField(max_length=50, blank=True)
    # profile_picture


class Game(models.Model):
    name = models.TextField(max_length=50, blank=True)
    gamemode = models.TextField(max_length=50, blank=True)
    players = models.ManyToManyField(Player)


class Chat(models.Model):
    name = models.TextField(max_length=50, blank=True)
    description = models.TextField(max_length=50, blank=True)
    profile_picture = models.TextField(max_length=50, blank=True)
    origin = models.TextField(max_length=50, blank=True)
