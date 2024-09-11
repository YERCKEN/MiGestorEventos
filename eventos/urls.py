from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    # Funciones
    path('eventos/', views.eventos, name='eventos'),
    path('crearEvento/', views.crearEvento, name='crearEvento'),
    
    path('editarEvento/<int:idEvento>/', views.editarEvento, name='editarEvento'),
    
    
    # Clases
    path('organizadores/', views.Organizadores.as_view(), name='organizadores'),

    path('organizadores/nuevo', views.CrearOrganizador.as_view(), name='crearOrganizador'),
    
    # LOGIN
    path('login/',views.Login, name='login'),
    path('registro/', views.Registro, name='registro'),
    path('logout/', views.cerrarSesion, name='cerrarSesion'),
    
]
