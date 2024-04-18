# Generated by Django 5.0 on 2024-01-24 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0018_rename_mbps_cliente_mbps_f_cliente_mbps_w'),
        ('instalaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instalacion',
            name='brigada',
        ),
        migrations.RemoveField(
            model_name='instalacion',
            name='cliente',
        ),
        migrations.AddField(
            model_name='instalacion',
            name='brigada',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instalacion',
            name='cliente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
        ),
    ]