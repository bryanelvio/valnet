# Generated by Django 5.0 on 2023-12-27 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_alter_articulo_cantidad_alter_articulo_costo_and_more'),
        ('empleados', '0002_empleado_telefono_alter_empleado_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_utilizada', models.PositiveIntegerField()),
                ('fecha_uso', models.DateTimeField(auto_now_add=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.articulo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleado')),
            ],
            options={
                'db_table': 'Uso de Articulos',
            },
        ),
    ]