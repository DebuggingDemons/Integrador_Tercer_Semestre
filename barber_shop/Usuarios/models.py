from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    usuarioFK = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=25)
    esBarbero = models.BooleanField() # True o False
    direccion = models.CharField(max_length=50)
    
