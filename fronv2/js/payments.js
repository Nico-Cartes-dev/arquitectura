function registerPayment(doctor, amount, paymentDate, paymentMethod) {
    // Simulación de registro de pago
    const confirmation = {
        doctorName: doctor,
        amount: parseFloat(amount).toFixed(2),
        date: paymentDate,
        method: paymentMethod,
        transactionNumber: Math.floor(Math.random() * 1000000) + 100000
    };

    return confirmation;
}

function registerPatientPayment(patient, service, amount, paymentMethod) {
    // Simulación de registro de pago del paciente
    const receipt = {
        patient: patient,
        service: service,
        amount: parseFloat(amount).toFixed(2),
        method: paymentMethod,
        dateTime: new Date().toLocaleString(),
        receiptNumber: Math.floor(Math.random() * 1000000) + 100000
    };

    return receipt;
}