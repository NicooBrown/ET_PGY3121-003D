from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "apellido", "correo", "numero_telefono", "comentario"]

class CustomCreationForm(UserCreationForm):
    pass