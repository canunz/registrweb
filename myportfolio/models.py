from django.db import models

# Create your models here.

class Evento(models.Model):
    # Define los campos del modelo Evento
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    # Otros campos necesarios

    def __str__(self):
        return self.nombre
    