from django.db import models

class usoBrigada(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null = False, auto_now_add=True)
    hora = models.TimeField(null = False, auto_now_add=True)
    brigada = models.ForeignKey('brigadas.Brigada', on_delete=models.SET_NULL, null=True, blank=True)
    articulos_usados = models.TextField(max_length=1000, null=True)
    cliente = models.CharField(max_length=100, null=True)
    razon = models.CharField(max_length=100, null=True)
    
    class Meta:
        db_table = 'uso'
        verbose_name = 'Uso'
        verbose_name_plural = 'Usos'

    def __str__(self):
        return self.id
