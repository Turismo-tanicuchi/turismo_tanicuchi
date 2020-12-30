from django.contrib import admin
from .models import TipoAC,AtractivoCultural
# Register your models here.
admin.site.register(TipoAC)

class AtractivoCulturalAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','direccion','latitud','longitud','tipo_id','parroquia')
    search_fields=('nombre','parroquia')
    list_filter=('parroquia','nombre')

admin.site.register(AtractivoCultural,AtractivoCulturalAdmin)
