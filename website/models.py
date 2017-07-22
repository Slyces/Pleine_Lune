from django.db import models

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=50, blank=True)
    # profile picture
    # game
    # Role
    # etat
    # Droits

class Role(models.Model):
    name = models.TextField(max_length=50, blank=True)
    description = models.TextField(max_length=500, blank=True)
    officiel = models.BooleanFieldField(blank=True)
    # profile_picture

class Game(models.Model):
    name = models.TextField(max_length=50, blank=True)
    gamemode = models.TextField(max_length=50, blank=True)
    players = models.ManyToManyField()
    # etat

class Message(models.Model):
    content = models.TextField(max_length=500, blank=True)
    # sender
    # tag
    # Date
    # game