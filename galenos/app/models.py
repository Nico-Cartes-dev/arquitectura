from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.especialidad})"

# Modelo de Disponibilidad del Doctor
class Disponibilidad(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='disponibilidades')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.fecha} {self.hora_inicio}-{self.hora_fin}"

# Modelo de Cita
class Cita(models.Model):
    paciente = models.CharField(max_length=255)  # Nombre del paciente
    rutpaciente = models.CharField(max_length=12)  # RUT del paciente
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    correo= models.EmailField()

    def __str__(self):
        return f"Cita con {self.doctor.name} para {self.paciente} el {self.fecha} a las {self.hora}"