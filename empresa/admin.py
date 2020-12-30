from django.contrib import admin
from empresa.models import TipoEmp,Empresa,Producto
# Register your models here.
class TipoAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','parroquia')
    search_fields=('nombre','descripcion')
    list_filter=('nombre',)

admin.site.register(TipoEmp,TipoAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','detalle','imagen','created_at')
    search_fields=('nombre','detalle')
    list_filter=('nombre',)
admin.site.register(Producto,ProductoAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','latitud','longitud','descripcion','tipo_id')
    search_fields=('nombre','descripcion')
    list_filter=('nombre',)

admin.site.register(Empresa,EmpresaAdmin)
