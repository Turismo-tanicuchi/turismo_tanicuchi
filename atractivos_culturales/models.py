from django.db import models
from parroquias.models import Parroquia
# Create your models here.

class TipoAC(models.Model):
    nombre_tipo_ac = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'TipoAC'
        verbose_name_plural = 'Tipos de Atractivos Culturales'
        ordering = ['nombre_tipo_ac']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre_tipo_ac

class AtractivoCultural(models.Model):
    nombre = models.CharField('Nombre del Atractivo',max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=100)
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='atractivos_cultuales/',blank=True, null=True)
    tipo_id = models.ForeignKey(TipoAC, on_delete=models.CASCADE,verbose_name="Tipo de atractivo")
    fecha = models.DateField(blank=True, null=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, verbose_name="Parroquia")
    # para conocer cuanto una atractivo_cultural se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'AtractivoCultural'
        verbose_name_plural = 'Atractivos Culturales'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
