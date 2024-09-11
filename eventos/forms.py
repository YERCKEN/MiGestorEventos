from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


from  . import models

# forms de Eventos -------------------------------------------------------------
class EventoForm(forms.ModelForm):
    
    #llenamoss el list box
    organizador = forms.ModelChoiceField(
        queryset= models.Organizador.objects.all(),
        required=True,
        empty_label="Selecciona un organizador"
    )
    
    # Campo fecha
    fecha = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd', 'class': 'pequeI'})
        # clase para estilo
    )
    
    # Campo hora
    hora = forms.TimeField(

        widget=forms.TextInput(attrs={'placeholder': 'hh:mm', 'class': 'pequeI'})

    )
    

    class Meta:
        model = models.Eventos
        fields = ['nombre', 'hora', 'fecha', 'lugar', 'descripcion', 'organizador']
        
    #funcuion para validar el campo nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        
        if "Cancelado" in nombre:
            raise forms.ValidationError("'Cancelado' No es un nombre válido")
        return nombre




# forms de login --------------------------------------------------------------
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    
# forms REGISTRO  --------------------------------------------------------------
class RegistroForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña'}))

    class Meta:
        model = User
        fields = ['username']

    # fuNCION PARA VALIDAR LA CONTRASEÑA SI ES IGUAL
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']