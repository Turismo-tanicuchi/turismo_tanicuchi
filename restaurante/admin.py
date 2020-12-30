from django.contrib import admin

# Register your models here.
from restaurante.models import Restaurante
# Register your models here.
#definimos que campos se visualizan en pantalla
class RestauranteAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','direccion','parroquia')
    search_fields=('nombre','descripcion',)
    list_filter=('nombre',)

admin.site.register(Restaurante,RestauranteAdmin)
