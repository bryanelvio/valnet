# Generated by Django 5.0 on 2023-12-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0004_registrouso'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrouso',
            name='uso',
            field=models.CharField(choices=[('ins', 'Instalacion'), ('rep', 'Reporte')], default='ins', max_length=3),
        ),
    ]
