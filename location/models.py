from django.db import models

# Create your models here.

class Region(models.Model):
    libRegion = models.CharField(max_length=30)

    def __str__(self):
        return self.libRegion


class Prefecture(models.Model):
    liPrefecture = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.liPrefecture


class Commune(models.Model):
    libCommune = models.CharField(max_length=30)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)

    def __str__(self):
        return self.libCommune


class Canton(models.Model):
    libCanton = models.CharField(max_length=30)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.libCanton


class Village(models.Model):
    libVillage = models.CharField(max_length=30)
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)

    def __str__(self):
        return self.libVillage


class Quartier(models.Model):
    libQuartier = models.CharField(max_length=30)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)

    def __str__(self):
        return self.libQuartier


