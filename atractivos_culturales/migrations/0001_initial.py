# Generated by Django 3.0.8 on 2020-11-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtractivoCultural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('longitud', models.CharField(blank=True, max_length=200, null=True)),
                ('latitud', models.CharField(blank=True, max_length=200, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='atractivos_cultuales/')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'AtractivoCultural',
                'verbose_name_plural': 'Atractivos Culturales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoAC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_ac', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'TipoAC',
                'verbose_name_plural': 'Tipos de Atractivos Culturales',
                'ordering': ['nombre_tipo_ac'],
            },
        ),
    ]
