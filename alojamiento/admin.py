from django.contrib import admin
from alojamiento.models import Alojamiento
# Register your models here.
class AlojamientoAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','latitud','longitud','descripcion')
    search_fields=('nombre','descripcion')
    list_filter=('nombre',)

admin.site.register(Alojamiento,AlojamientoAdmin)
