from django.db import models

# Create your models here.
class familiares(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    trabajador = models.BooleanField()
    pariente = models.CharField(default="Hermano", max_length=100)
