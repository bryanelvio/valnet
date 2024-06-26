# Generated by Django 5.0 on 2023-12-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0005_registrouso_uso'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='articulo',
            name='fecha_ingreso',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='articulo',
            name='ubicacion',
            field=models.CharField(default='Almacen', max_length=50),
        ),
    ]
