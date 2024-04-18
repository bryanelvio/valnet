# Generated by Django 5.0 on 2023-12-27 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0017_remove_cliente_ip_cliente_ip_activo'),
        ('ips', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ip',
            old_name='is_active',
            new_name='activo',
        ),
        migrations.AddField(
            model_name='ip',
            name='usadopor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cliente'),
        ),
    ]
