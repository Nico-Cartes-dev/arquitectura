from django.contrib import admin

# Register your models here.
from .models import Doctor, Disponibilidad, Cita

# Configuración para el modelo Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'especialidad')  # Mostrar nombre y especialidad en la lista
    search_fields = ('name', 'especialidad')  # Agregar barra de búsqueda por nombre y especialidad
    list_filter = ('especialidad',)  # Filtro por especialidad

# Configuración para el modelo Disponibilidad
@admin.register(Disponibilidad)
class DisponibilidadAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'fecha', 'hora_inicio', 'hora_fin')  # Mostrar los campos importantes
    search_fields = ('doctor__name', 'fecha')  # Buscar por nombre del doctor y fecha
    list_filter = ('fecha', 'doctor')  # Filtros por fecha y doctor

# Configuración para el modelo Cita
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'rutpaciente', 'doctor', 'fecha', 'hora')  # Mostrar campos relevantes
    search_fields = ('paciente', 'rutpaciente', 'doctor__name')  # Buscar por paciente, RUT y doctor
    list_filter = ('fecha', 'doctor')  # Filtros por fecha y doctor
    date_hierarchy = 'fecha'  # Barra de navegación por fechas