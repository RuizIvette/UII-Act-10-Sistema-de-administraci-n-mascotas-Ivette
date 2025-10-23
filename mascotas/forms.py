# mascotas/forms.py
from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'especie', 'fecha_nacimiento']
        labels = {
            'nombre': 'Nombre',
            'raza': 'Raza',
            'especie': 'Especie',
            'fecha_nacimiento': 'Fecha de Nacimiento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }