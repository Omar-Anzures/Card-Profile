from django.db import models


class Perfil(models.Model):
    nombre=models.CharField(max_length=200)
    puesto=models.CharField(max_length=100)
    descripccion=models.TextField()