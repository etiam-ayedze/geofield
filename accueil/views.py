from django.shortcuts import render
from django.db import connection

# Create your views here.

def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM qgis_parcelles")
        result = cursor.fetchall()

    return render(request, 'accueil/accueil.html', locals())

