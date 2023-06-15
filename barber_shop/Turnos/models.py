from django.db import models

# Create your models here.
class Turno(models.Model):

    idTurno = models.IntegerField
    idCliente = models.ForeignKey(Usuarios, on_delete=models. CASCADE)
    idProf = models.ForeignKey(Usuarios, on_delete=models. CASCADE)
    idServicio = models.ForeignKey(Servicios, on_delete=models. CASCADE)
    detalle = models.CharField(max_length=200)
    fechaHora = models.DateTimeField

    def __str__(self) -> str:
        return f'''
            Id Turno: {self.idTurno},
            Id Cliente: {self.idCliente},
            Id Profesional: {self.idProf},
            Id Servicio: {self.idServicio},
            Detalles:  {self.detalle},
            Fecha: {self.fechaHora}        
        '''
