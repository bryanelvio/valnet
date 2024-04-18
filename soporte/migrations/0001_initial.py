# Generated by Django 5.0 on 2023-12-10 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(max_length=50)),
                ('lugar', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
                ('brigada', models.CharField(blank=True, max_length=50, null=True)),
                ('solucion', models.CharField(blank=True, max_length=100, null=True)),
                ('camisa', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
