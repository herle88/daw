from django.db import models

class Administrador(models.Model):
    nombre = models.CharField(max_length=20, unique = True)
    password = models.CharField(max_length=20)