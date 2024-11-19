const doctorField = document.getElementById('doctor');
const fechaField = document.getElementById('fecha');
const horaField = document.getElementById('hora');

function fetchHorasDisponibles() {
    const doctorId = doctorField.value;
    const fecha = fechaField.value;
    if (doctorId && fecha) {
        fetch(`/reservar-hora/?doctor_id=${doctorId}&fecha=${fecha}`)
            .then(response => response.json())
            .then(data => {
                horaField.innerHTML = '<option value="" disabled selected>Seleccione una hora</option>';
                data.horas_disponibles.forEach(hora => {
                    const option = document.createElement('option');
                    option.value = hora;
                    option.textContent = hora;
                    horaField.appendChild(option);
                });
            });
    }
}

doctorField.addEventListener('change', fetchHorasDisponibles);
fechaField.addEventListener('change', fetchHorasDisponibles);