from django.db import models
from lugar import Lugar

class Sector(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    precio = models.IntegerField(blank=True, null=True)
    cantidadEntrdas = models.IntegerField(blank=True, null=True)
    entradasVendidas = models.IntegerField(blank=True, null=True)
    lugar = models.ForeignKey(Lugar, blank=True, null=True)

