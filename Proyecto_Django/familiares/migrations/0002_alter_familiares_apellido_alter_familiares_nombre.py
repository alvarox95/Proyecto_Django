# Generated by Django 4.1.4 on 2022-12-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='familiares',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
