
def hospital(patient, doctor, date):
    doctors = ["Dr. Smith", "Dr. John", "Dr. Emily"]

    if doctor in doctors:
        return (
            "Appointment booked successfully!\n"
            "Patient Name: " + patient + "\n"
            "Doctor: " + doctor + "\n"
            "Date: " + date
        )
    else:
        return "Doctor not available"
