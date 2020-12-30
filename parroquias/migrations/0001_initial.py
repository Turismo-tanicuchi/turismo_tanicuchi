# Generated by Django 3.0.8 on 2020-11-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesParroquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='parroquias/')),
            ],
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_parr', models.CharField(max_length=50, verbose_name='Nombre de la parroquia')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección ')),
                ('longitud', models.CharField(blank=True, max_length=200, null=True)),
                ('latitud', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='parroquias/')),
                ('historia', models.TextField(blank=True, null=True, verbose_name='Historia')),
                ('info_general', models.TextField(blank=True, null=True, verbose_name='Información General')),
                ('situacion_geografica', models.TextField(blank=True, null=True, verbose_name='Situación Geográfica')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='documentos/', verbose_name='pdf')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Parroquia',
                'verbose_name_plural': 'Parroquias',
                'ordering': ['nombre_parr'],
            },
        ),
    ]