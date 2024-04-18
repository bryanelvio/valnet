from django.db import models
from empleados.models import Empleados


class Brigada(models.Model):
    id = models.AutoField(primary_key=True)
    ficha = models.CharField(max_length=3)
    placa = models.CharField(max_length=100)
    lider = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.ficha + ' - ' + self.placa
    
    
class articuloBrigada(models.Model):
    id = models.AutoField(primary_key=True)
    brigada = models.ForeignKey('Brigada', on_delete=models.CASCADE)
    articulo = models.CharField(max_length=50, null=True)
    cantidad = models.IntegerField(null=True)
    medida = models.CharField(max_length=20, null=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.articulo + ' - ' + self.brigada
       
