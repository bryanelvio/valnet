# Generated by Django 5.0 on 2024-01-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brigadas', '0009_alter_brigada_lider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articuloinventario',
            name='ubicacion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
