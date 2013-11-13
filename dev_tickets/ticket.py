from django.db import models
from sector import Sector
from espectaculo import Espectaculo

class Ticket(models.Model):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    documento = models.CharField(max_length=10, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    sector = models.OneToOneField(Sector)
    espectaculo = models.ForeignKey(Espectaculo, blank=True, null=True)
