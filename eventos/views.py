from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models
# importamos los forms
from . import forms


def eventos (request):
    
    eventos = models.Eventos.objects.all()
    
    return render(request, 'eventos.html', {'eventos': eventos, })


def crearEvento(request):
    
    if request.method == 'POST':
        form = forms.EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos') 
    else:
        form = forms.EventoForm()
    
    return render(request, 'crearEventos.html', {'form': form}) 