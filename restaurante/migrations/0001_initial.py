# Generated by Django 3.0.8 on 2020-11-28 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parroquias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('direccion', models.CharField(max_length=100)),
                ('longitud', models.CharField(max_length=200)),
                ('latitud', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='restaurantes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parroquias.Parroquia', verbose_name='Parroquia')),
            ],
            options={
                'verbose_name': 'Restaurante',
                'verbose_name_plural': 'Restaurantes',
                'ordering': ['nombre'],
            },
        ),
    ]
