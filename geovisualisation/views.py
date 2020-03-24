from django.shortcuts import render, HttpResponse, redirect, get_list_or_404, get_object_or_404
from djgeojson.views import GeoJSONLayerView
from lands.models import Parcelle
from django.contrib.auth.decorators import login_required

from lands.models import Proprietaire, Typesuccession, Typeparcelle, Parcelle, HistoriqueProprio, Fichier
# Create your views here.
@login_required
def visualize(request):
    parcelle = Parcelle.objects.all()
    return render(request, 'geovisualisation/visualize.html', locals())


class ParcelleVue(GeoJSONLayerView):
    geometry_field = 'coordonee'
    model = Parcelle
    properties = ('numLot',)

