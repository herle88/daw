from django.db import models
from categoria import Categoria
from lugar import Lugar

class Espectaculo(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False, null=True)
    hora = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    estado = models.NullBooleanField()
    imagen = models.CharField(max_length=50, blank=True)
    categoria = models.ForeignKey(Categoria, blank=True, null=True)
    lugar = models.OneToOneField(Lugar)
