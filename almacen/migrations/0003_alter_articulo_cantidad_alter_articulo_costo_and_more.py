# Generated by Django 5.0 on 2023-12-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_alter_articulo_medida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='costo',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='medida',
            field=models.CharField(max_length=20),
        ),
    ]
