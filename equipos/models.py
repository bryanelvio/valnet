from django.db import models
from clientes.models import Cliente

class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=20, null=False)
    marca = models.CharField(max_length=20, null=False)
    modelo = models.CharField(max_length=50, null=False)
    serie = models.CharField(max_length=50)
    mac = models.CharField(max_length=50, null=True)
    pass_wifi = models.CharField(max_length=50, null=True)
    clave = models.CharField(max_length=50, null=True)
    usuario = models.CharField(max_length=50, null=True)
    ubicacion = models.CharField(max_length=50, default='Almacen')
    instalado = models.BooleanField(default=False)
    c_instalado = models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True, blank=True)
 
    def __str__(self):
        return self.marca + ' ' + self.modelo + ' ' + self.serie