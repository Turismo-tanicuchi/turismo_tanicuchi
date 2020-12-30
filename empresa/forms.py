from django import forms
from empresa.models import Empresa,Producto,TipoEmp

class FormularioCategoriaEmpresa(forms.ModelForm):
    class Meta:
        model = TipoEmp
        fields = ('nombre','descripcion','imagen','parroquia')
        labels = {
            #como quiero que se vean los labels
            'nombre': 'Nombre de la Categoria',
            'descripcion':'Ingrese una descripción corta de la categoria que no exceda los 125 caracteres',
            'imagen': 'Cargue una Imagen que represente a la categoria',
            'parroquia':'Seleccione la parroquia'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la empresa',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            ),
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
                    'type':'hidden'
                }
            )
        }

class FormularioEmpresa(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Empresa
        fields = ('nombre','direccion','latitud','longitud','descripcion','imagen','tipo_id')
        labels = {
            #como quiero que se vean los labels
            'nombre': 'Nombre de la empresa',
            'direccion':'Dirección',
            'latitud': 'coordenadas Latitud',
            'longitud':'coordenadas Longitud',
            'descripcion':'Descripción',
            'imagen': 'Imagen',
            'tipo_id': 'Tipo de empresa'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la empresa',
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
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'tipo_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione el tipo',
                }
            )
        }

class FormularioEditEmpresa(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Empresa
        fields = ('nombre','direccion','latitud','longitud','descripcion','imagen','tipo_id')
        labels = {
            #como quiero que se vean los labels
            'nombre': 'Nombre de la empresa',
            'direccion':'Dirección',
            'latitud': 'coordenadas Latitud',
            'longitud':'coordenadas Longitud',
            'descripcion':'Descripción',
            'imagen': 'Imagen',
            'tipo_id': 'Tipo de empresa'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la empresa',
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
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'tipo_id': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la categoría',
                    #que no se pueda cambiar
                    'readonly':'readonly',
                    #que no se vea
                    'type':'hidden'
                }
            )
        }

class FormularioProducto(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Producto
        fields = ('nombre','detalle','imagen','empresa')
        #empresa = forms.ModelChoiceField(queryset=Empresa.objects.filter(tipo_id__parroquia__id__administrador__id=self.user.id).order_by('nombre'))

        labels = {
            #como quiero que se vean los labels
            'nombre': 'Nombre del producto',
            'detalle':'Detalle del producto no debe exceder de los 300 caracteres',
            'imagen': 'Imagen',
            'empresa':'Elija la empresa'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto',
                }
            ),
            'detalle': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'empresa': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la empresa',
                }
            )
        }

class FormularioEditProducto(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Producto
        fields = ('nombre','detalle','imagen','empresa')
        #empresa = forms.ModelChoiceField(queryset=Empresa.objects.filter(tipo_id__parroquia__id__administrador__id=self.user.id).order_by('nombre'))

        labels = {
            #como quiero que se vean los labels
            'nombre': 'Nombre del producto',
            'detalle':'Detalle del producto no debe exceder de los 300 caracteres',
            'imagen': 'Imagen',
            'empresa':'Elija la empresa'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto',
                }
            ),
            'detalle': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una detalle del producto',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'empresa': forms.TextInput(
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
