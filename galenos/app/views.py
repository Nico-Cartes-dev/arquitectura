from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_date
from .models import Doctor, Cita, Disponibilidad
from .utils import DOCTORES
from .utils import enviar_correo_confirmacion_cita
from datetime import timedelta, datetime

# Create your views here.
def admin_cajero(request):
    return render(request, 'core/admin-cajero.html')

def admin_medico(request):
    return render(request, 'core/admin-medico.html')

def admin_paciente(request):
    return render(request, 'core/admin-paciente.html')

def admin_secretaria(request):
    return render(request, 'core/admin-secretaria.html')

def anular_hora(request):
    return render(request, 'core/anular-hora.html')

def espera_hora(request):
    return render(request, 'core/consultar-pacientes-espera.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def doctores_planta(request):
    return render(request, 'core/doctores.html')

def emitir_comprobante_comision(request):
    return render(request, 'core/emitir-comprobante-comision.html')

def generar_calendario(request):
    return render(request, 'core/generar-calendario-agenda.html')

def index(request):
    return render(request, 'core/index.html')

def informe_recaudacion(request):
    return render(request, 'core/informe-recaudacion.html')

def ingresar_disponibilidad(request):
    return render(request, 'core/ingresar-disponibilidad.html')

def ingresar_pago_paciente(request):
    return render(request, 'core/ingresar-pago-paciente.html')

def modificar_agenda(request):
    return render(request, 'core/modificar-agenda.html')

def registrar_pago_comisiones(request):
    return render(request, 'core/registrar-pago-comisiones.html')

# Función para validar el formato del RUT chileno
def es_rut_valido(rut):
    # El formato del RUT chileno es como: 12.345.678-9
    # Vamos a quitar los puntos y validar el RUT
    rut = rut.replace('.', '').replace('-', '')
    if len(rut) < 9 or len(rut) > 10:
        return False
    rut_body = rut[:-1]
    rut_verifier = rut[-1]
    
    # Validar si el cuerpo del RUT es numérico
    if not rut_body.isdigit():
        return False
    
    # Validar el dígito verificador (último número)
    if rut_verifier not in '0123456789kK':
        return False
    return True


def reservar_hora(request):
    doctores = Doctor.objects.all()

    # Verificamos si es un POST
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        rut = request.POST.get('rut')
        correo = request.POST.get('correo')
        doctor_id = request.POST.get('doctor')  # El ID del doctor seleccionado
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        # Validaciones de los campos
        if not nombre or not rut or not correo or not doctor_id or not fecha or not hora:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('reservar_hora')

        if not es_rut_valido(rut):  # Debes tener esta función definida
            messages.error(request, "El RUT ingresado no es válido.")
            return redirect('reservar_hora')

        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            messages.error(request, "El médico seleccionado no existe.")
            return redirect('reservar_hora')

        # Convertir la fecha
        fecha_obj = parse_date(fecha)
        if fecha_obj is None:
            messages.error(request, "La fecha proporcionada no es válida.")
            return redirect('reservar_hora')

        # Verificar si ya hay una cita en esa hora
        if Cita.objects.filter(doctor=doctor, fecha=fecha_obj, hora=hora).exists():
            messages.error(request, f"La hora {hora} ya está ocupada por otro paciente.")
            return redirect('reservar_hora')

        # Crear la cita
        Cita.objects.create(
            paciente=nombre,
            rutpaciente=rut,
            correo=correo,
            doctor=doctor,
            fecha=fecha_obj,
            hora=hora
        )

        messages.success(request, "¡Cita reservada con éxito!")
        return redirect('index')

    # Si es un GET, obtener las horas disponibles
    horas_disponibles = []
    if 'doctor' in request.GET and 'fecha' in request.GET:
        doctor_id = request.GET['doctor']
        fecha = request.GET['fecha']
        doctor = Doctor.objects.get(id=doctor_id)
        fecha_obj = parse_date(fecha)

        if fecha_obj:
            # Filtramos las disponibilidades del doctor en esa fecha
            disponibilidades = Disponibilidad.objects.filter(doctor=doctor, fecha=fecha_obj)

            # Verificamos que existan disponibilidades y las agregamos a horas_disponibles
            if disponibilidades.exists():
                for disponibilidad in disponibilidades:
                    horas_disponibles.append(f"{disponibilidad.hora_inicio} - {disponibilidad.hora_fin}")
            else:
                messages.error(request, "No hay horas disponibles para el doctor en esta fecha.")
                return redirect('reservar_hora')

    # Verificamos si las horas se están pasando correctamente
    horas_disponibles = list(set(horas_disponibles))  # Eliminar duplicados
    horas_disponibles.sort()  # Ordenar las horas

    return render(request, 'core/reservar-hora.html', {
        'doctores': doctores,
        'horas_disponibles': horas_disponibles,  # Pasar las horas disponibles al template
    })
def servicios(request):
    return render(request, 'core/servicios.html')




    

