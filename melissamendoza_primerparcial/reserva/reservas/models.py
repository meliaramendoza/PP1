from django.db import models

from django.db import models

class Hotel(models.Model):
    identificador = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()


class Reserva(models.Model):
    id = models.CharField(max_length=20, unique=True)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    num_huespedes = models.PositiveIntegerField()
    TIPO_HABITACION_CHOICES = (
        ('S', 'Simple'),
        ('D', 'Doble'),
        ('T', 'Triple'),
    )
    tipo_habitacion = models.CharField(max_length=1, choices=TIPO_HABITACION_CHOICES)
    precio_total = models.DecimalField(max_digits=8, decimal_places=2)
    ESTADO_RESERVA_CHOICES = (
        ('C', 'Confirmada'),
        ('CA', 'Cancelada'),
        ('E', 'En espera'),
    )
    estado_reserva = models.CharField(max_length=2, choices=ESTADO_RESERVA_CHOICES)
