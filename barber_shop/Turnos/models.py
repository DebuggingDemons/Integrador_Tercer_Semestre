from django.db import models

from Usuarios.models import Usuario

# Create your models here.
class Turno(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    usuario = models.ForeignKey(Usuario, on_delete=models. CASCADE)
    profesional = models.ForeignKey(Usuario, on_delete=models. CASCADE, related_name='turno_profesional', default=None)
    # idServicio = models.ForeignKey(Servicios, on_delete=models. CASCADE)
    detalle = models.CharField(max_length=200)
    fechaHora = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'''
            Id Cliente: {self.cliente},
            Id Profesional: {self.profesional},
            Detalles:  {self.detalle},
            Fecha: {self.fechaHora}        
        '''
