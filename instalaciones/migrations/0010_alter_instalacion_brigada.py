# Generated by Django 5.0 on 2024-02-13 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brigadas', '0011_remove_brigadainventario_articulos_and_more'),
        ('instalaciones', '0009_alter_instalacion_brigada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacion',
            name='brigada',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brigadas.brigada'),
        ),
    ]
