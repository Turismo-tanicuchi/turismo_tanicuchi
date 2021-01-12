from django import forms
from parroquias.models import Parroquia,ImagenesParroquia

class FormularioParroquia(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Parroquia
        fields = ('nombre_parr','direccion','latitud','longitud','imagen','historia','info_general','situacion_geografica','email','telefono','celular','pdf')
        labels = {
            #como quiero que se vean los labels
            'nombre_parr': 'Nombre de la Parroquia',
            'direccion':'Dirección',
            'latitud': 'coordenadas Latitud',
            'longitud':'coordenadas Longitud',
            'imagen': 'Imagen',
            'historia':'historia',
            'info_general':'Informacion General',
            'situacion_geografica':' Situacion Geografica',
            'email': 'Ingrese el correo parroquial',
            'telefono': 'Ingrese el Teléfono de la parroquia',
            'celular': 'Ingrese el Celular si es necesario',
            'pdf': 'Cargue un pdf con más información de la parroquia si requiere',
        }
        widgets = {
            'nombre_parr': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la parroquia',
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
            'historia': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la historia',
                }
            ),
            'info_general': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la Información general',
                }
            ),
            'situacion_geografica': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ingrese la situación geográfica',
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                }
            ),
            'celular': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Celular',
                }
            ),
            'pdf': forms.FileInput(
                attrs = {
                    'placeholder': 'Cargue un archivo si desea',
                }
            ),
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

class FormularioImgParroquia(forms.ModelForm):
    class Meta:
        model = ImagenesParroquia
        fields = ('imagen','parroquia')
        labels = {
            'imagen': 'Imagen',
            'parroquia': 'Elija la parroquia'
        }
        widgets = {
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'parroquia': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la parroquia',
                    #que no se pueda cambiar
                    'readonly':'readonly',
                    #que no se vea
                    'type':"hidden"
                }
            )
        }
