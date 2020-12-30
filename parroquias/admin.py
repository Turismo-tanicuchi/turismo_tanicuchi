from django.contrib import admin
from .models import Parroquia,ImagenesParroquia

class ParroquiaAdmin(admin.ModelAdmin):
    fields = ('nombre_parr', 'direccion','longitud','latitud','imagen','historia','info_general','situacion_geografica','email','telefono','celular','administrador','pdf' )
    list_display = ('__str__','direccion','email','telefono','celular','slug','created_at')
    search_fields = ('__str__',)
    list_filter = ('nombre_parr',)

class ImgParroquiaAdmin(admin.ModelAdmin):
    list_display = ('imagen','parroquia')

# Register your models here.
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(ImagenesParroquia, ImgParroquiaAdmin)
