# Generated by Django 5.0 on 2023-12-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brigadas', '0002_remove_tecnico_nombre_tecnico_usuario_and_more'),
        ('empleados', '0006_rename_empleado_empleados'),
    ]

    operations = [
        migrations.AddField(
            model_name='brigada',
            name='lider',
            field=models.ManyToManyField(to='empleados.empleados'),
        ),
        migrations.DeleteModel(
            name='Tecnico',
        ),
    ]