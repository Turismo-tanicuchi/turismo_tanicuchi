# Generated by Django 3.0.8 on 2020-12-12 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0003_remove_transporte_tipo_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoTransporte',
        ),
    ]