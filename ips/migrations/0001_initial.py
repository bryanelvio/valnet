# Generated by Django 5.0 on 2023-12-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
