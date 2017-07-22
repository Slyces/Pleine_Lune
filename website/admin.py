from django.contrib import admin
from .models import *

# password : I am root

# Register your models here.
admin.site.register(Game)
admin.site.register(Message)
admin.site.register(Player)
admin.site.register(Role)