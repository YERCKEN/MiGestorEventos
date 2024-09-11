from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Eventos, Organizador



# importamos los forms
from . import forms
# para los formularios bassados en clases|
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# para los formulario de login y registro
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Vista de eventos ------------------------------------------------------------

def eventos (request):

    eventos = Eventos.objects.all().order_by('-id')
    return render(request, 'eventos.html', {'eventos': eventos, })

# Vista de crear eventos ------------------------------------------------------

@login_required
def crearEvento(request):
    
    if request.method == 'POST':
        
        form = forms.EventoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionamos a la vista de eventos
            return redirect('eventos') 
    else:
        
        form = forms.EventoForm()
    
    return render(request, 'eventosForms.html', {'form': form, 'creando': True}) 


# Nueva Vista para editar eventos ------------------------------------------------------
@login_required
def editarEvento(request, idEvento):
    
    evento = Eventos.objects.get(id=idEvento)
    
    if request.method == 'POST':
        
        form = forms.EventoForm(request.POST, instance=evento)
        
        if form.is_valid():
            
            print('Formulario valido')
            form.save()
            return redirect('eventos')
    else:
        
        print('Formulario invalido')
        form = forms.EventoForm(instance=evento)

    return render(request, 'eventosForms.html', {'form': form, 'creando': False})




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



def Login(request):
    if request.method == 'POST':
        
        form = forms.LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                return redirect('eventos')
    else:
        form = forms.LoginForm()
        
    return render(request, 'login.html', {'form': form})


# vista de Registro -----------------------------------------------------------

def Registro(request):
    if request.method == 'POST':
        
        form = forms.RegistroForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            
            return redirect('login')
    else:
        form = forms.RegistroForm()
        
    return render(request, 'registro.html', {'form': form})


def cerrarSesion(request):
    
    logout(request) 
    return redirect('eventos')