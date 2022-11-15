from django.db import models
from django.contrib import admin

# Create your models here.
class Connexion(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    creat_at = models.DateTimeField(auto_now_add=True)

class AdminConnexion(admin.ModelAdmin):
    list_display = ['username', 'password', 'creat_at']