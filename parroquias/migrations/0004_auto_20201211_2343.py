# Generated by Django 3.0.8 on 2020-12-12 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parroquias', '0003_auto_20201128_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parroquia',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='Dirección'),
        ),
    ]