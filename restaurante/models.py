from django.db import models
from parroquias.models import Parroquia

# Create your models here.
class Restaurante(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=500)
    direccion = models.CharField(max_length=100)
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='restaurantes/',blank=True, null=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, verbose_name="Parroquia")
    # para conocer cuando un restaurante se Registra
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Restaurante'
        verbose_name_plural = 'Restaurantes'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
