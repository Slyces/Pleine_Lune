from django.contrib import admin
from django.contrib.admin import register
from .models import *

# password : I am root

# Register your models here.
register(Game)
register(Message)
register(Player)
register(Role)