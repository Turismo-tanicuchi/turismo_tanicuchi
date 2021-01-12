from django.db import models
# Create your models here.
# modelo para ingresar informacion del proyecto como la mision vision etc.
class InformacionTurismo(models.Model):
    titulo = models.CharField('Titulo',max_length=150, unique=True)
    descripcion = models.TextField('Descripción')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'InformacionTurismo'
        verbose_name_plural = 'Informacion del sitio'
        ordering = ['titulo']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.titulo
