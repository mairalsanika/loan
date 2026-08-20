from HospitalManagement import hospital_bill

print("===== HOSPITAL QA TESTING =====")

hospital_bill("Patient1", "Dr.A", "General",
              "Normal", 30, 500, 500, "No", "No")

hospital_bill("Patient2", "Dr.B", "Emergency",
              "Emergency", 40, 1000, 1000, "No", "No")

hospital_bill("Patient3", "Dr.C", "General",
              "Normal", 30, 500, 700, "No", "Yes")

hospital_bill("Patient4", "Dr.D", "Cardiology",
              "Normal", 30, 1000, 1000, "Yes", "No")

hospital_bill("Patient5", "Dr.E", "General",
              "Follow-up", 20, 300, 400, "No", "No")

hospital_bill("Patient6", "Dr.F", "Cardiology",
              "Emergency", 60, 1500, 2000, "Yes", "No")

hospital_bill("Patient7", "Dr.G", "Neurology",
              "Normal", 40, 1000, 1500, "Yes", "Yes")

hospital_bill("Patient8", "Dr.H", "General",
              "Follow-up", 20, 300, 500, "No", "Yes")

hospital_bill("Patient9", "Dr.I", "Emergency",
              "Emergency", 30, 800, 1200, "No", "Yes")

hospital_bill("Patient10", "Dr.J", "Cardiology",
              "Emergency", 50, 2000, 2500, "Yes", "Yes")

print("===== QA TESTING COMPLETED =====")