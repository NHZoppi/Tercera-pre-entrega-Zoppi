from django import forms
from .models import Auto, Venta, Sucursal
import django_filters

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'año', 'patente', 'nombre_vendedor', 'precio', "sucursal"]

class VentaForm(forms.ModelForm):
    class Meta:
        widgets = {
            'fecha': forms.TextInput(attrs={'type':'date'}),
        }
        model = Venta
        fields = ['auto', 'comprador_nombre', 'precio_venta', 'fecha']

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'direccion', 'ciudad', 'estado', 'pais','telefono']

class AutoFilter(django_filters.FilterSet):
    marca = django_filters.CharFilter(lookup_expr= "iexact")
    modelo = django_filters.CharFilter(lookup_expr= "iexact")
    class Meta:
        model = Auto
        fields = ['patente']