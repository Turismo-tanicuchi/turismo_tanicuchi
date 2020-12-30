from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuario.models import Usuario


# Register your models here.
#user admin personalizado
#class UserAdmin(admin.ModelAdmin):
#    list_display=('id','first_name','last_name','email')
#    search_fields=('username','email')
#    list_filter=('email',)

#mediante esta funcion agregamos los campos adicionales del useradmin
class MyUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('direccion','imagen','usuario_admin')}),
    )

admin.site.register(Usuario,MyUserAdmin)
