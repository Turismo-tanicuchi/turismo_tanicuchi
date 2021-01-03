from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from usuario.models import Usuario
import uuid
# Create your models here.

class Parroquia(models.Model):
    nombre_parr = models.CharField('Nombre de la parroquia',max_length=50, unique=True)
    direccion = models.CharField('Dirección',max_length=50)
    latitud = models.CharField(max_length=200,blank=True, null=True)
    longitud = models.CharField(max_length=200,blank=True, null=True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    imagen = models.ImageField(upload_to='parroquias/',blank=True, null=True)
    historia = models.TextField('Historia',blank=True, null=True)
    info_general = models.TextField('Información General',blank=True, null=True)
    situacion_geografica=models.TextField('Situación Geográfica',blank=True, null=True)
    email = models.EmailField('Correo')
    telefono = models.CharField('Teléfono',max_length=10)
    celular = models.CharField('Celular',max_length=10,blank=True, null=True)
    pdf = models.FileField('pdf',upload_to='documentos/', blank=True, null=True)
    administrador = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name="administrador")

    # para conocer cuanto una parroquias se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Parroquia'
        verbose_name_plural = 'Parroquias'
        ordering = ['nombre_parr']

    #def save(self, *arg, **Kwargs):
    #    self.slug = slugify(self.nombre_parr)
    #    super(Parroquia,self).save(*arg, **Kwargs)

    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre_parr

#generar slug unico
def set_slug(sender, instance, *args, **kwargs):  #callback
    if instance.nombre_parr and not instance.slug:
        slug = slugify(instance.nombre_parr)
        while Parroquia.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.nombre_parr,str(uuid.uuid4())[:8])
            )
        instance.slug = slug
#antes de guardar ejecute slug
pre_save.connect(set_slug, sender=Parroquia)

class ImagenesParroquia(models.Model):
    imagen = models.ImageField(upload_to='parroquias/')
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Parroquia")
