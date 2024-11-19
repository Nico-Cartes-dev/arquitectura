from django.urls import path
from .views import (
    admin_cajero, admin_medico, admin_paciente, admin_secretaria, anular_hora,
    espera_hora, contacto, doctores_planta, emitir_comprobante_comision, 
    generar_calendario, index, informe_recaudacion, ingresar_disponibilidad,
    ingresar_pago_paciente, modificar_agenda, registrar_pago_comisiones, 
    reservar_hora, servicios
)

urlpatterns = [
    # Ruta principal (index)
    path('', index, name='index'),
    
    # Paneles de administración
    path('admin/cajero/', admin_cajero, name='admin_cajero'),
    path('admin/medico/', admin_medico, name='admin_medico'),
    path('admin/paciente/', admin_paciente, name='admin_paciente'),
    path('admin/secretaria/', admin_secretaria, name='admin_secretaria'),
    
    # Anular hora
    path('anular-hora/', anular_hora, name='anular_hora'),
    
    # Consultar pacientes en espera
    path('consultar/pacientes/espera/', espera_hora, name='espera_hora'),
    
    # Sección de contacto
    path('contacto/', contacto, name='contacto'),
    
    # Doctores
    path('doctores/', doctores_planta, name='doctores_planta'),
    
    # Emitir comprobante de comisión
    path('emitir/comprobante/comision/', emitir_comprobante_comision, name='emitir_comprobante_comision'),
    
    # Reservar hora
    path('reservar-hora/', reservar_hora, name='reservar_hora'),
    
    # Informe de recaudación
    path('informe/recaudacion/', informe_recaudacion, name='informe_recaudacion'),
    
    # Ingresar disponibilidad
    path('ingresar/disponibilidad/', ingresar_disponibilidad, name='ingresar_disponibilidad'),
    
    # Ingresar pago paciente
    path('ingresar/pago/paciente/', ingresar_pago_paciente, name='ingresar_pago_paciente'),
    
    # Modificar agenda
    path('modificar/agenda/', modificar_agenda, name='modificar_agenda'),
    
    # Registrar pago de comisiones
    path('registrar/pago/comisiones/', registrar_pago_comisiones, name='registrar_pago_comisiones'),
    
    # Servicios
    path('servicios/', servicios, name='servicios'),
    
    # Generar calendario (si se usa)
    path('generar/calendario/', generar_calendario, name='generar_calendario'),
]
