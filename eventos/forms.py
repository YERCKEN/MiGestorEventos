from django import forms
from  . import models

class EventoForm(forms.ModelForm):
    
    #llenabos el list box
    organizador = forms.ModelChoiceField(
        queryset= models.Organizador.objects.all(),
        required=True,
        empty_label="Selecciona un organizador"
    )
    
    fecha = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.TextInput(attrs={'placeholder': 'dd-mm-yyyy'})
    )
    
    class Meta:
        model = models.Eventos
        fields = ['nombre', 'hora', 'fecha', 'lugar', 'descripcion', 'organizador']
    
    #funcuion para validar el campo nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if "Cancelado" in nombre:
            raise forms.ValidationError("El nombre del evento no puede contener la palabra 'Cancelado'.")
        return nombre
