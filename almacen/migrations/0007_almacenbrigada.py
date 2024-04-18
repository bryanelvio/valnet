# Generated by Django 5.0 on 2023-12-30 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0006_articulo_fecha_actualizacion_articulo_fecha_ingreso_and_more'),
        ('empleados', '0006_rename_empleado_empleados'),
    ]

    operations = [
        migrations.CreateModel(
            name='almacenBrigada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('brigada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleados')),
                ('inventario', models.ManyToManyField(to='almacen.articulo')),
            ],
        ),
    ]
