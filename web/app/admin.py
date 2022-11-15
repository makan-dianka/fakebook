from django.contrib import admin
from . models import Connexion, AdminConnexion

# Register your models here.
admin.site.register(Connexion, AdminConnexion)
