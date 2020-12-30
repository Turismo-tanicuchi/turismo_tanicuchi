from django.db import models
from django.contrib.auth.models import AbstractUser
#para autocompletar username
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.


class Usuario(AbstractUser):
    first_name = models.CharField('Nombres',max_length=100)
    last_name = models.CharField('Apellidos',max_length=100)
    email = models.EmailField('correo', unique=True)
    username = models.CharField('nombre de usuario', max_length=150, blank=True, null=True)
    direccion = models.CharField('Direccion',max_length=500, blank=True, null=True)
    imagen = models.ImageField('Imagen de perfil',upload_to='perfil/', null=True,blank=True, max_length=200)
    usuario_admin = models.BooleanField('Administrador parroquial', default=False) #todo usuario en true puede ser admin
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']

def set_username(sender, instance, *args, **kwargs):  #callback
    #autocompletar username
    if instance.first_name and not instance.username:
        username = slugify(instance.first_name+' '+instance.last_name)
        instance.username = username
#antes de guardar ejecute

pre_save.connect(set_username, sender=Usuario)
