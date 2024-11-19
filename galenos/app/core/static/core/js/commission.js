document.addEventListener('DOMContentLoaded', function() {
    const commissionForm = document.getElementById('commissionForm');
    const commissionDetails = document.getElementById('commissionDetails');
    const printButton = document.getElementById('printButton');

    commissionForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const doctor = document.getElementById('doctor').value;
        const startDate = document.getElementById('startDate').value;
        const endDate = document.getElementById('endDate').value;
        generateCommissionReport(doctor, startDate, endDate);
    });

    function generateCommissionReport(doctor, startDate, endDate) {
        // Simulación de generación de reporte
        const report = {
            doctorName: document.getElementById('doctor').options[document.getElementById('doctor').selectedIndex].text,
            period: `${startDate} al ${endDate}`,
            totalConsultations: Math.floor(Math.random() * 50) + 10,
            totalCommission: (Math.random() * 1000 + 500).toFixed(2)
        };

        document.getElementById('doctorName').textContent = report.doctorName;
        document.getElementById('period').textContent = report.period;
        document.getElementById('totalConsultations').textContent = report.totalConsultations;
        document.getElementById('totalCommission').textContent = report.totalCommission;

        commissionDetails.style.display = 'block';
    }

    printButton.addEventListener('click', function() {
        window.print();
    });
});