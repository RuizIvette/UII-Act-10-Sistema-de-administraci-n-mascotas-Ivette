# mascotas/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Mascota
from .forms import MascotaForm

def index(request):
    """Muestra la lista de todas las mascotas."""
    return render(request, 'mascotas/index.html', {
        'mascotas': Mascota.objects.all()
    })

def view_mascota(request, id):
    """Redirecciona al índice después de ver detalles (ya que se usa un modal)."""
    return HttpResponseRedirect(reverse('index'))

def add(request):
    """Permite añadir una nueva mascota."""
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save() # Guarda el formulario directamente ya que es un ModelForm
            return render(request, 'mascotas/add.html', {
                'form': MascotaForm(),
                'success': True
            })
    else:
        form = MascotaForm()
    return render(request, 'mascotas/add.html', {
        'form': form
    })

def edit(request, id):
    """Permite editar los datos de una mascota existente."""
    mascota = get_object_or_404(Mascota, pk=id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return render(request, 'mascotas/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'mascotas/edit.html', {
        'form': form
    })

def delete(request, id):
    """Permite eliminar una mascota."""
    if request.method == 'POST':
        mascota = get_object_or_404(Mascota, pk=id)
        mascota.delete()
    return HttpResponseRedirect(reverse('index'))