# Generated by Django 3.0.8 on 2020-12-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_auto_20201128_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoemp',
            name='descripcion',
            field=models.TextField(blank=True, max_length=125, null=True),
        ),
    ]