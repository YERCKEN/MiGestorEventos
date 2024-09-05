from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.eventos, name='eventos'),
    path('crearEvento/', views.crearEvento, name='crearEvento'),
]
