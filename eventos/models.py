from django.db import models

# MODELOS

# eventos y organizador y evento 

#Un organizador puede gestionar varios eventos, pero un
#evento solo puede tener un organizador. Usa ForeignKey para definir esta relación.

class Eventos(models.Model):
    
    nombre = models.CharField(max_length=150)
    # HORA Y FECHA
    hora = models.TimeField()
    fecha = models.DateField()
    
    lugar = models.CharField(max_length=100)
    
    descripcion = models.TextField()
    
    organizador = models.ForeignKey("organizador", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Organizador(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre