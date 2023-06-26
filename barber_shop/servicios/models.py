from django.db import models

class Servicios(models.Model):
    idServicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=False)
    descripcion = models.CharField(max_length=200, blank=False)
    precio = models.DecimalField(max_length=10, blank=False, decimal_places=2, max_digits=10,
                                 validators=[MinValueValidator(0.01)])

    def __str__(self) -> str:
            return f'''
                Id Servicio: {self.idServicio},
                nombre: {self.nombre},
                Descripcion: {self.descripcion},
                Precio: {self.precio}        
            '''                                 

