# Generated by Django 5.0 on 2024-02-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalaciones', '0005_alter_instalacion_brigada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacion',
            name='brigada',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
