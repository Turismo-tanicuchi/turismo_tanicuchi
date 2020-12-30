from django import forms
from restaurante.models import Restaurante

class FormularioRestaurante(forms.ModelForm):
    #registros
    class Meta:
        model = Restaurante
        fields = ('nombre','descripcion','direccion','latitud','longitud','imagen','parroquia')
        labels = {
            #como quiero que se vena los labels
            'nombre': 'Nombre de Restaurante',
            'descripcion':'Ingrese la descripción del lugar',
            'direccion':'Dirección',
            'latitud': 'Coordenadas Latitud',
            'longitud':'Coordenadas Longitud',
            'imagen':'Cargue una imagen referente al restaurante',
            'parroquia':'Elija la parroquia'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de Restaurante',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion',
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección',
                }
            ),
            'longitud': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'longitud',
                }
            ),
            'latitud': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'latitud',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'Cargue una imagen',
                }
            ),
            'parroquia': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la parroquia',
                    #que no se pueda cambiar
                    'readonly':'readonly',
                    #que no se vea
                    'type':'hidden'
                }
            )
        }
#--------------------------- MAGALY--------------------------------------------------------------------
    def clean_latitud(self):
        latitud = self.cleaned_data.get('latitud')
        if str(latitud).isalpha():
            raise forms.ValidationError('El campo "Latitud" no puede ser alfabetico"')
        return latitud

    def clean_longitud(self):
        longitud = self.cleaned_data.get('longitud')
        if str(longitud).isalpha():
            raise forms.ValidationError('El campo "Longuitud" no puede ser alfabetico"')
        return longitud
#------------------------------------------------------------------------------------------------------
