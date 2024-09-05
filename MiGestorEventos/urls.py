

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    
    #URLS DEL APP eventos
    path("", include("eventos.urls")),
]
