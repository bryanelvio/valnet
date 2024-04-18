# Generated by Django 5.0 on 2024-02-13 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brigadas', '0011_remove_brigadainventario_articulos_and_more'),
        ('instalaciones', '0002_remove_instalacion_brigada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacion',
            name='brigada',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='brigadas.brigada'),
        ),
    ]