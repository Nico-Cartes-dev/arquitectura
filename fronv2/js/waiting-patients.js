document.addEventListener('DOMContentLoaded', function() {
    const waitingPatientsTable = document.getElementById('waitingPatients').getElementsByTagName('tbody')[0];

    // Simulación de datos de pacientes en espera
    const patients = [
        { name: 'Juan Pérez', appointmentTime: '10:00', status: 'En espera' },
        { name: 'María García', appointmentTime: '10:30', status: 'En consulta' },
        { name: 'Carlos Rodríguez', appointmentTime: '11:00', status: 'En espera' }
    ];

    patients.forEach(patient => {
        const row = waitingPatientsTable.insertRow();
        row.innerHTML = `
            <td>${patient.name}</td>
            <td>${patient.appointmentTime}</td>
            <td>${patient.status}</td>
        `;
    });
});