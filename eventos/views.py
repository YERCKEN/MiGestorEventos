from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Eventos, Organizador



# importamos los forms
from . import forms
# para los formularios bassados en clases|
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# Vista de eventos ------------------------------------------------------------

def eventos (request):
    
    eventos = Eventos.objects.all()
    
    return render(request, 'eventos.html', {'eventos': eventos, })

# Vista de crear eventos ------------------------------------------------------

def crearEvento(request):
    
    if request.method == 'POST':
        
        form = forms.EventoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionamos a la vista de eventos
            return redirect('eventos') 
    else:
        
        form = forms.EventoForm()
    
    return render(request, 'crearEventos.html', {'form': form}) 


# Vista de organizadores basada en clases -------------------------------------
class Organizadores(ListView):
    model = Organizador
    template_name = 'organizadores.html'
    context_object_name = 'organizadores'
    
    
# Vista de crear organizadores basada en clases --------------------------------
class CrearOrganizador(CreateView):
    
    model = Organizador
    fields = ['nombre', 'apellido']
    template_name = 'crearOrganizadores.html'
    success_url = reverse_lazy('organizadores') 
    
# Vista de login --------------------------------------------------------------


# vista de Registro -----------------------------------------------------------