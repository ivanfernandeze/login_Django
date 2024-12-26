from django import forms
from .models import Categoria, Unidad

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['descripcion', 'estado']

class CategoriaFormSinEstado(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion']

class UnidadFormSinEstado(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['descripcion']