from django.db import models
from clientes.models import Cliente
from brigadas.models import Brigada

# Create your models here.
class Instalacion(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True)
    brigada = models.ForeignKey(Brigada, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(auto_now_add=True)
    materiales = models.CharField(max_length=1000, null=True)
    instalado = models.BooleanField(default=False)
    nota = models.TextField(max_length=1000, null=True)
    class Meta:
        db_table = 'instalaciones'