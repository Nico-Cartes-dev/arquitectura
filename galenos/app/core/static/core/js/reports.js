function generateReport(startDate, endDate) {
    // Simulación de datos de recaudación
    const reportData = [
        { date: '2024-03-01', consultations: 15, revenue: 1500 },
        { date: '2024-03-02', consultations: 12, revenue: 1200 },
        { date: '2024-03-03', consultations: 18, revenue: 1800 },
    ];

    let reportHTML = '<table><thead><tr><th>Fecha</th><th>Consultas</th><th>Recaudación</th></tr></thead><tbody>';
    reportData.forEach(day => {
        reportHTML += `<tr><td>${day.date}</td><td>${day.consultations}</td><td>$${day.revenue}</td></tr>`;
    });
    reportHTML += '</tbody></table>';

    return reportHTML;
}