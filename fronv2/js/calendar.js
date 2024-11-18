function generateCalendar(month, year) {
    const daysInMonth = new Date(year, month, 0).getDate();
    const firstDay = new Date(year, month - 1, 1).getDay();

    let calendarHTML = `<h3>${getMonthName(month)} ${year}</h3>`;
    calendarHTML += '<table>';
    calendarHTML += '<tr><th>Dom</th><th>Lun</th><th>Mar</th><th>Mié</th><th>Jue</th><th>Vie</th><th>Sáb</th></tr>';

    let day = 1;
    for (let i = 0; i < 6; i++) {
        calendarHTML += '<tr>';
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                calendarHTML += '<td></td>';
            } else if (day > daysInMonth) {
                calendarHTML += '<td></td>';
            } else {
                calendarHTML += `<td>${day}</td>`;
                day++;
            }
        }
        calendarHTML += '</tr>';
        if (day > daysInMonth) {
            break;
        }
    }

    calendarHTML += '</table>';
    return calendarHTML;
}

function getMonthName(month) {
    const monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
    return monthNames[month - 1];
}