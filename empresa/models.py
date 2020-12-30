from django.db import models
from parroquias.models import Parroquia
# Create your models here.

class TipoEmp(models.Model):
    nombre = models.CharField('Categoria',max_length=100, unique=True)
    descripcion = models.CharField('Descripcion',blank=True, max_length=125, null=True)
    imagen = models.ImageField(upload_to='tipo_empresa/',blank=True, null=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, verbose_name="Parroquia")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'Categoria de la empresa'
        verbose_name_plural = 'Categoria'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
class Empresa(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)    
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='empresa/',blank=True, null=True)
    tipo_id = models.ForeignKey(TipoEmp, on_delete=models.CASCADE,verbose_name="Categoria")

    # para conocer cuando  se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    detalle = models.CharField('Descripción',max_length=300)
    imagen = models.ImageField(upload_to='productos/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,verbose_name="Empresa")
    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural = 'Productos de la empresa'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
