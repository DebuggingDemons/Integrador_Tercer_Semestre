from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    telefono = models.CharField(max_length=25)
    esBarbero = models.BooleanField() # True o False
    direccion = models.CharField(max_length=50)

    
