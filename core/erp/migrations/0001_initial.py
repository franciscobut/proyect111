# Generated by Django 4.0.2 on 2022-02-07 02:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50, verbose_name='Nombres')),
                ('curp', models.CharField(max_length=18, verbose_name='Curp')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_creation', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('state', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
                ('cvitae', models.FileField(blank=True, null=True, upload_to='cvitae/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
    ]
