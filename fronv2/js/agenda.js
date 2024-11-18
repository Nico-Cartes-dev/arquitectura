document.addEventListener('DOMContentLoaded', function() {
    const agendaForm = document.getElementById('agendaForm');
    const agendaTable = document.getElementById('agendaTable');
    const agendaTableBody = document.getElementById('agendaTableBody');

    agendaForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const doctor = document.getElementById('doctor').value;
        const date = document.getElementById('date').value;
        loadAgenda(doctor, date);
    });

    function loadAgenda(doctor, date) {
        // Simulación de citas para el médico en la fecha seleccionada
        const appointments = [
            { time: '09:00', patient: 'Ana García' },
            { time: '10:00', patient: 'Carlos Rodríguez' },
            { time: '11:00', patient: 'María López' },
            { time: '12:00', patient: 'Juan Martínez' },
        ];

        agendaTableBody.innerHTML = '';
        appointments.forEach((appointment, index) => {
            const row = agendaTableBody.insertRow();
            row.innerHTML = `
                <td>${appointment.time}</td>
                <td>${appointment.patient}</td>
                <td>
                    <button onclick="editAppointment(${index})">Editar</button>
                    <button onclick="deleteAppointment(${index})">Eliminar</button>
                </td>
            `;
        });

        agendaTable.style.display = 'block';
    }

    window.editAppointment = function(index) {
        alert(`Editando cita ${index + 1}`);
    }

    window.deleteAppointment = function(index) {
        if (confirm(`¿Está seguro de que desea eliminar la cita ${index + 1}?`)) {
            alert(`Cita ${index + 1} eliminada`);
        }
    }
});