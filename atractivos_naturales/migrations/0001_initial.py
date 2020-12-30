# Generated by Django 3.0.8 on 2020-11-28 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtractivoNatural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_an', models.CharField(max_length=100, verbose_name='Nombre del atractivo Natural')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('direccion_an', models.CharField(blank=True, max_length=100, null=True)),
                ('longitud_an', models.CharField(blank=True, max_length=200, null=True)),
                ('latitud_an', models.CharField(blank=True, max_length=200, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='atractivos_naturales/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'AtractivoNatural',
                'verbose_name_plural': 'Atractivos Naturales',
                'ordering': ['nombre_an'],
            },
        ),
        migrations.CreateModel(
            name='TipoAN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_an', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'TipoAN',
                'verbose_name_plural': 'Tipos de Atractivos Naturales',
                'ordering': ['nombre_tipo_an'],
            },
        ),
        migrations.CreateModel(
            name='ImagenesAtractivoNatural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='atractivos_naturales/')),
                ('atractivo_natural', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atractivos_naturales.AtractivoNatural', verbose_name='Atractivo Natural')),
            ],
        ),
    ]
