# Generated by Django 5.0 on 2023-12-30 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0008_remove_almacenbrigada_brigada_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='almacenbrigada',
            table='Uso de Articulos',
        ),
        migrations.DeleteModel(
            name='RegistroUso',
        ),
    ]
