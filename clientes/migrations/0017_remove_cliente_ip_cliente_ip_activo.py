# Generated by Django 5.0 on 2023-12-27 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_alter_cliente_cedula_alter_cliente_rnc_and_more'),
        ('ips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='ip',
        ),
        migrations.AddField(
            model_name='cliente',
            name='ip_activo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ips.ip'),
        ),
    ]
