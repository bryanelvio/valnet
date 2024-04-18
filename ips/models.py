from django.db import models

class Ip(models.Model):
    id = models.AutoField(primary_key=True)
    num = models.CharField(max_length=50, null = False)
    activo = models.BooleanField(default=False)
    usedby = models.ForeignKey('clientes.Cliente', on_delete=models.SET_NULL, null=True, blank=True)