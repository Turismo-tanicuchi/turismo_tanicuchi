from django.db import models
from parroquias.models import Parroquia
# Create your models here.

class TipoAN(models.Model):
    nombre_tipo_an = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'TipoAN'
        verbose_name_plural = 'Tipos de Atractivos Naturales'
        ordering = ['nombre_tipo_an']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre_tipo_an

class AtractivoNatural(models.Model):
    nombre = models.CharField('Nombre del atractivo Natural',max_length=100, unique=True)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=100)
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)
    tipo_id = models.ForeignKey(TipoAN, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='atractivos_naturales/',blank=True, null=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, verbose_name="Parroquia")
    # para conocer cuanto una atractivo_naturales se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'AtractivoNatural'
        verbose_name_plural = 'Atractivos Naturales'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre

class ImagenesAtractivoNatural(models.Model):
    imagen = models.ImageField(upload_to='atractivos_naturales/',blank=True, null=True)
    atractivo_natural = models.ForeignKey(AtractivoNatural, on_delete=models.CASCADE, verbose_name="Atractivo Natural")
