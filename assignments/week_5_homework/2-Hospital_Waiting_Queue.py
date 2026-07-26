patients = ['Rin', 'Sam', 'Yuki']
patients.append('Leo')
calling_patients = patients.pop(0)
print(f"calling patient: {calling_patients}")
print(f"remaining queue: {patients}")
print(f"Patients waiting: {len(patients)}")