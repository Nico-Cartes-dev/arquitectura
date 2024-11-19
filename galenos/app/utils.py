from datetime import datetime, timedelta
from .models import Doctor, Disponibilidad, Cita  # Asegúrate de importar los modelos correctamente

DOCTORES = [
    {"name": "Dr. Juan Pérez", "especialidad": "Cardiología"},
    {"name": "Dra. María González", "especialidad": "Neurología"},
    {"name": "Dr. Carlos Rodríguez", "especialidad": "Pediatría"},
    {"name": "Dra. Ana Martínez", "especialidad": "Dermatología"},
    {"name": "Dr. Luis Fernández", "especialidad": "Oftalmología"},
    {"name": "Dra. Patricia López", "especialidad": "Ginecología"},
    {"name": "Dr. Jorge Sánchez", "especialidad": "Traumatología"},
    {"name": "Dra. Laura García", "especialidad": "Psiquiatría"},
    {"name": "Dr. Roberto Díaz", "especialidad": "Medicina General"},
    {"name": "Dra. Carmen Hernández", "especialidad": "Oncología"}
]

def generar_horas_disponibles(disponibilidad, citas):
    """
    Genera un listado de horas disponibles para un doctor en una fecha específica.
    
    disponibilidad: instancia de Disponibilidad.
    citas: listado de citas existentes para el doctor en esa fecha.
    """
    hora_actual = datetime.combine(disponibilidad.fecha, disponibilidad.hora_inicio)
    hora_fin = datetime.combine(disponibilidad.fecha, disponibilidad.hora_fin)
    
    citas_ocupadas = {cita.hora for cita in citas}  # Crear un set con las horas ocupadas

    horas_disponibles = []
    while hora_actual.time() < hora_fin.time():
        if hora_actual.time() not in citas_ocupadas:
            horas_disponibles.append(hora_actual.time())  # Solo agregar horas no ocupadas
        hora_actual += timedelta(minutes=30)  # Incrementar en intervalos de 30 minutos

    return horas_disponibles

def obtener_horas_disponibles(doctor_id, fecha):
    """
    Obtiene las horas disponibles para un doctor específico en una fecha dada.
    
    doctor_id: ID del doctor en la base de datos.
    fecha: fecha para la que se desea conocer la disponibilidad.
    """
    # Obtener el doctor
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        return []  # Si no existe el doctor, devolver lista vacía

    # Obtener la disponibilidad del doctor para esa fecha
    disponibilidad = Disponibilidad.objects.filter(doctor=doctor, fecha=fecha).first()

    if not disponibilidad:
        return []  # Si no hay disponibilidad para ese doctor en esa fecha, devolver lista vacía

    # Obtener las citas existentes para el doctor en esa fecha
    citas = Cita.objects.filter(doctor=doctor, fecha=fecha)

    # Generar las horas disponibles
    horas_disponibles = generar_horas_disponibles(disponibilidad, citas)

    return horas_disponibles

# Ejemplo de uso
# doctor_id = 1  # El id del doctor, este será dinámico según la petición
# fecha = datetime(2024, 11, 19).date()  # La fecha para la cual buscamos la disponibilidad

# horas = obtener_horas_disponibles(doctor_id, fecha)
# print(f"Horas disponibles para el doctor en la fecha {fecha}: {horas}")


from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import render

def enviar_correo_confirmacion_cita(request, cita):
    """
    Envía un correo electrónico de confirmación de cita médica al paciente.
    """
    try:
        # Configuración del correo
        subject = 'Confirmación de Reserva de Cita Médica'
        recipient_list = [cita.correo]  # Dirección de correo del paciente

        # Generar el contenido del correo
        message = render(request, 'email/confirmacion_cita.html', {
            'paciente': cita.paciente,
            'doctor': cita.doctor.name,
            'especialidad': cita.doctor.especialidad,
            'fecha': cita.fecha,
            'hora': cita.hora,
        })

        # Enviar el correo
        send_mail(
            subject=subject,
            message='',  # El texto plano no se usa porque estamos enviando un HTML
            recipient_list=recipient_list,
            html_message=message.content.decode('utf-8')
        )
        return True
    except Exception as e:
        print(f"Error enviando correo: {e}")
        return False