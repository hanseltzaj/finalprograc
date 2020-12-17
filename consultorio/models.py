from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    nombre = models.CharField(max_length=120)
    fechanacimiento = models.DateTimeField(blank=True, null=False)
    direccion = models.CharField(max_length=180)
    telefono = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    fecha = models.DateTimeField(blank=True, null=False)
    paciente = models.ForeignKey(
        Paciente, related_name="citas", on_delete=models.CASCADE
    )
    estado = models.CharField(max_length=10, blank=True, null=True)

    def atender(self):
        self.estado = "Atendido"
        self.save

    def __str__(self):
        return self.fecha

class Medicamento(models.Model):
    nombre = models.CharField(max_length=180)
    dosis = models.CharField(max_length=180)

    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    fecha_creacion = models.DateTimeField('Creado', default=timezone.now)
    paciente = models.ForeignKey(
        Paciente, related_name="consultas", on_delete=models.CASCADE
    )
    sintomas = models.TextField()
    medicamento = models.ForeignKey(
        Medicamento, related_name="medicamentos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.fecha_creacion
