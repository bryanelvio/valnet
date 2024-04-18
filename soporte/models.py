from django.db import models
from brigadas.models import Brigada
from clientes.models import Cliente

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=True)
    brigada = models.ForeignKey(Brigada, on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    f_reg = models.DateField(auto_now_add=True)
    f_compromiso = models.DateField(null=True)
    prioridad = models.CharField(max_length=50, default='Regular')
    hora = models.TimeField(auto_now_add=True)
    descripcion = models.TextField(max_length=1000, null=True)
    solucionado = models.BooleanField(default=False)
    solucion = models.TextField(max_length=1000, null=True)
    nota = models.TextField(max_length=1000, null=True)
    class Meta:
        db_table = 'tickets'
        
    def __str__(self):
        return str(self.id) + ' - ' + self.titulo