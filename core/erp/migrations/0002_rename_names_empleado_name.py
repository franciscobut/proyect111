# Generated by Django 4.0.2 on 2022-02-07 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='names',
            new_name='name',
        ),
    ]
