from django import forms
from .models import Proprietaire, Typesuccession, Typeparcelle, Fichier, Parcelle, HistoriqueProprio
from django.contrib.gis import forms


class proprio_form(forms.ModelForm):
    class Meta:
        model = Proprietaire
        fields = "__all__"


class typesuccession_form(forms.ModelForm):
    class Meta:
        model = Typesuccession
        fields = "__all__"


class typeparcelle_form(forms.ModelForm):
    class Meta:
        model = Typeparcelle
        fields ="__all__"


class fichier_form(forms.ModelForm):
    class Meta:
        model = Fichier
        fields ="__all__"

class parcelle_form(forms.ModelForm):
    class Meta:
        model = Parcelle
        fields ="__all__"
    # numLot = forms.CharField(max_length=30)
    # numTitreFoncier = forms.CharField(max_length=30)
    # numIdFiscal = forms.CharField(max_length=30)
    # numApprobation = forms.CharField(max_length=30)
    # dide = forms.CharField(max_length=30)
    # nomGeometre = forms.CharField(max_length=30)
    # surface = forms.FloatField
    # typeParcelle = forms.IntegerField
    # quartier = forms.IntegerField
    # coordonee = forms.PolygonField

class historique_proprio_form(forms.Form):
    class Meta:
        model = HistoriqueProprio
        fields ="__all__"
    # proprietaire = forms.IntegerField
    # parcelle = forms.IntegerField
    # file = forms.CharField(max_length=254)
    # typeSuccession = forms.IntegerField
    # dateDebutPossession = forms.DateField
    # dateFinPossession = forms.DateField

