# Generated by Django 5.0 on 2023-12-28 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0004_equipo_delete_router'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='fecha_instalado',
        ),
    ]
