from django.contrib import admin
from .models import TipoAN,AtractivoNatural,ImagenesAtractivoNatural
# Register your models here.
admin.site.register(TipoAN)
admin.site.register(ImagenesAtractivoNatural)
class AtractivoNaturalAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','direccion','latitud','longitud','tipo_id')
    search_fields=('nombre','descripcion')
    list_filter=('nombre',)

admin.site.register(AtractivoNatural,AtractivoNaturalAdmin)
