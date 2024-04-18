from django.db import models


class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, null=True)
    costo = models.IntegerField(null=True)
    cantidad = models.IntegerField(null=True)
    medida = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField(auto_now_add=True, null=True)
    fecha_salida = models.DateTimeField(auto_now_add=True, null=True)