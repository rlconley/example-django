from django.contrib import admin
from .models import Game

# Register your models here.
admin.site.register(Game)
# telling the Django admin that we have a new model