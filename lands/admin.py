from django.contrib import admin
from lands.models import HistoriqueProprio, Parcelle, Proprietaire, Fichier

# Register your models here.
admin.site.register(HistoriqueProprio)
admin.site.register(Parcelle)
admin.site.register(Proprietaire)
admin.site.register(Fichier)