# Generated by Django 3.0.8 on 2020-12-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0004_delete_tipotransporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporte',
            name='ruta',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
