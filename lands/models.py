from django.db import models
from phone_field import PhoneField
from django.contrib.gis.db import models
from location.models import Quartier

# Create your models here.
class Proprietaire(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1)
    telephone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    fonction = models.CharField(max_length=25)
    date_naiss = models.DateField(default=None)
    num_pieceid = models.CharField(max_length=15)

    def __str__(self):
        return self.nom+' '+self.prenom



class Typesuccession(models.Model):
    libTypeSuccession = models.CharField(max_length=30)

    def __str__(self):
        return self.libTypeSuccession



class Typeparcelle(models.Model):
    libTypeParcelle = models.CharField(max_length=30)

    def __str__(self):
        return self.libTypeParcelle



class Parcelle(models.Model):
    numLot = models.CharField(max_length=30)
    numTitreFoncier = models.CharField(max_length=30)
    numIdFiscal = models.CharField(max_length=30)
    numApprobation = models.CharField(max_length=30)
    dide = models.CharField(max_length=30)
    nomGeometre = models.CharField(max_length=30)
    surface = models.FloatField(null=True)
    typeParcelle = models.ForeignKey(Typeparcelle, on_delete=models.CASCADE)
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)

    coordonee = models.PolygonField()

    def __str__(self):
        return self.numLot

class HistoriqueProprio(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE)
    typeSuccession = models.ForeignKey(Typesuccession, on_delete=models.CASCADE)
    dateDebutPossession = models.DateField(null=True)
    dateFinPossession = models.DateField(null=True)

    def __str__(self):
        return self.proprietaire.nom + self.proprietaire.prenom + self.parcelle.numLot



class Fichier(models.Model):
    file = models.CharField(max_length=255)
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE)
    def __str__(self):
        return self.file











