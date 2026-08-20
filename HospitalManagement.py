def hospital_bill(patient, doctor, department, appointment,
                  duration, lab_charge, medicine_charge,
                  insurance, senior):

    
    consultation_fee = duration * 100

    
    if appointment == "Emergency":
        consultation_fee += 500

    
    if senior == "Yes":
        consultation_fee *= 0.80


    if appointment == "Follow-up":
        consultation_fee *= 0.50

    
    total = consultation_fee + lab_charge + medicine_charge

    
    if insurance == "Yes":
        insurance_amount = total * 0.70
    else:
        insurance_amount = 0

    patient_amount = total - insurance_amount

    print("-----------------------------")
    print("Patient:", patient)
    print("Doctor:", doctor)
    print("Department:", department)
    print("Consultation Fee:", consultation_fee)
    print("Lab Charges:", lab_charge)
    print("Medicine Charges:", medicine_charge)
    print("Insurance Coverage:", insurance_amount)
    print("Patient Payable:", patient_amount)
    print("-----------------------------")


# Examples - No input required

hospital_bill("Rahul", "Dr. Sharma", "Cardiology",
              "Normal", 30, 500, 800, "No", "No")

hospital_bill("Priya", "Dr. Mehta", "Neurology",
              "Emergency", 40, 1000, 1500, "Yes", "No")

hospital_bill("Ravi", "Dr. Kumar", "General",
              "Follow-up", 20, 300, 500, "Yes", "Yes")