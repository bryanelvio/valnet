# Generated by Django 5.0 on 2024-02-09 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brigadas', '0010_alter_articuloinventario_ubicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brigadainventario',
            name='articulos',
        ),
        migrations.RemoveField(
            model_name='brigada',
            name='articulos',
        ),
        migrations.CreateModel(
            name='articuloBrigada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('articulo', models.CharField(max_length=50, null=True)),
                ('cantidad', models.IntegerField(null=True)),
                ('medida', models.CharField(max_length=20, null=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, null=True)),
                ('brigada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brigadas.brigada')),
            ],
        ),
        migrations.DeleteModel(
            name='articuloInventario',
        ),
        migrations.DeleteModel(
            name='brigadaInventario',
        ),
    ]
