from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    telefono = models.CharField(max_length=25)
    esBarbero = models.BooleanField(default=False) # True o False
    direccion = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='123456abc!')
    username = models.CharField(max_length=50, default='username', unique=True)

    
