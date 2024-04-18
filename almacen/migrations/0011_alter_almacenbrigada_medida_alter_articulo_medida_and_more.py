# Generated by Django 5.0 on 2023-12-30 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0010_alter_almacenbrigada_table'),
        ('empleados', '0006_rename_empleado_empleados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacenbrigada',
            name='medida',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='medida',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='RegistroUso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('ins', 'Instalacion'), ('rep', 'Reporte')], default='ins', max_length=3)),
                ('cantidad_utilizada', models.PositiveIntegerField()),
                ('fecha_uso', models.DateTimeField(auto_now_add=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.articulo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleados')),
            ],
            options={
                'db_table': 'Uso de Articulos',
            },
        ),
    ]
