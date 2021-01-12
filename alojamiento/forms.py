from django import forms
from alojamiento.models import Alojamiento

class FormularioAlojamientos(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Alojamiento
        fields = ('nombre','direccion','latitud','longitud','imagen','descripcion','parroquia')
        labels = {
            #como quiero que se vean los labels
            'nombre': 'Nombre del Alojamiento',
            'direccion':'Dirección',
            'latitud': 'coordenadas Latitud',
            'longitud':'coordenadas Longitud',
            'imagen': 'Imagen',
            'descripcion':'Descripción',
            'parroquia': 'Elige la parroquia'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del Alojamiento',
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección',
                }
            ),
            'latitud': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'latitud',
                }
            ),
            'longitud': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'longitud',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
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

#-------------- Magaly - Validacion -----------------------------------------------
    def clean_latitud(self):
        latitud = self.cleaned_data.get('latitud')
        if str(latitud).isalpha():
            raise forms.ValidationError('El campo "Latitud" no puede ser alfabetico')
        else:
            for i in range(len(str(latitud))):
                if str(latitud)[i].isspace():
                    raise forms.ValidationError('El campo no puede tener espacios en blanco')
        return latitud

    def clean_longitud(self):
        longitud = self.cleaned_data.get('longitud')
        if str(longitud).isalpha():
            raise forms.ValidationError('El campo "Longuitud" no puede ser alfabetico')
        else:
            for i in range(len(str(longitud))):
                if str(longitud)[i].isspace():
                    raise forms.ValidationError('El campo no puede tener espacios en blanco')
        return longitud
