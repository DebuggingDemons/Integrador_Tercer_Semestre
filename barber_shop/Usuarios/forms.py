from django import forms
from .models import Usuario

class formularioDeLogin(forms.Form):
        username =  forms.CharField(max_length=100)
        password =  forms.CharField(widget= forms.PasswordInput())
        
        class Meta:
            model = Usuario
    
class formularioDeREgistro(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    verificacion_password = forms.CharField(widget=forms.PasswordInput())
    email =  forms.EmailField()
    nombre =  forms.CharField()
    apellido =  forms.CharField()
    esBarbero =  forms.CheckboxInput()
        
    class Meta:
        model =  Usuario
