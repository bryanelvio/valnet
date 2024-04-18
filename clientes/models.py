from django.db import models
from ips.models import Ip


class Cliente(models.Model):
    
    
    ## Datos del Cliente ##
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    apellidos = models.CharField(max_length=100, null=True)
    cedula = models.CharField(max_length=100, null=True)
    rnc = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    zona = models.CharField(max_length=100, null=True)
    direccion = models.TextField(max_length=100, null=True)
    plan = models.CharField(max_length=50, null=True)
    mbps_w = models.CharField(max_length=50, null=True)
    mbps_f = models.CharField(max_length=50, null=True)
    tipo = models.CharField(max_length=50, null=True)
    f_nac = models.DateField(null=True)
    f_reg = models.DateField(auto_now_add=True, null=True)
    subida = models.CharField(max_length=50, null=True)
    bajada = models.CharField(max_length=50, null=True)


    ## Datos de configuracion ##
    
    ppp = models.CharField(max_length=50, null=True, blank=True)
    c_nap = models.CharField(max_length=50, null=True)
    ip_activo = models.ForeignKey(Ip, on_delete=models.SET_NULL, null=True)
    mac = models.CharField(max_length=50, null=True)
    emisor = models.CharField(max_length=50 , null=True)
    instalado = models.DateTimeField(null=True)
    
    class Meta:
        db_table = 'clientes'
        
    ## Retorno de titular en la vista ##
    def __str__(self):
        return self.nombre
