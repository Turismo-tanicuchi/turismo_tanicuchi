from django.db import models
from parroquias.models import Parroquia
# Create your models here.

class Transporte(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ruta = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='transportes/',blank=True, null=True)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, verbose_name="Parroquia")
    observaciones = models.CharField(max_length=500,blank=True, null=True)
    # para conocer cuanto una atractivo_cultural se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Transporte'
        verbose_name_plural = 'Transportes'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
