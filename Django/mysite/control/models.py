from django.db import models

#EMPLEADOS
class Empleado(models.Model):
    TURNOS = [
        ('Día', 'Día'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    ]

    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, unique=True)
    departamento = models.CharField(max_length=100)
    fecha_inicio = models.DateField(auto_now_add=True)
    dias_trabajo = models.CharField(max_length=50)
    turno = models.CharField(max_length=10, choices=TURNOS)
    horario_entrada = models.TimeField()
    horario_salida = models.TimeField()

    def __str__(self):
        return self.nombre

#JORNADA
class Jornada(models.Model):
    TIPOS_MARCACION = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]

    identificador = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    tipo_marcacion = models.CharField(max_length=10, choices=TIPOS_MARCACION)

    def __str__(self):
        return f'Jornada {self.identificador} - Empleado: {self.empleado.nombre}'
