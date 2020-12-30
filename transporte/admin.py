from django.contrib import admin
from .models import Transporte
# Register your models here.

class TransporteAdmin(admin.ModelAdmin):
    list_display=('nombre','ruta','imagen','observaciones','parroquia')
    search_fields=('nombre','ruta')
    list_filter=('nombre',)

admin.site.register(Transporte,TransporteAdmin)
