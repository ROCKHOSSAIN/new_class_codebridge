patients_list_info = []
priority_count=0
Normal_Treatment_count=0
Standard_Treatment_count=0
while True:
    patient_name=input("Enter patient name (or 'done'): ")
    if patient_name=="done":
        i=0
        while i<len(patients_list_info):
            print(f"{patients_list_info[i][0]}|  Age: {patients_list_info[i][1]} | Severity: {patients_list_info[i][2]} -> {patients_list_info[i][3]}")
            i+=1
        break

    patient_name = patient_name.title()
    age=int(input("Enter age: "))
    severity=int(input("Enter severity (1-10): "))
    patients_list_info.append([patient_name,age,severity])
    if age>=60 or severity>=7:
       treatment_type="Priority Treatment" 
       priority_count+=1
       patients_list_info[-1].append(treatment_type)
    elif age>=18 or severity>=4:
        treatment_type="Normal Treatment"
        Normal_Treatment_count+=1
        patients_list_info[-1].append(treatment_type)
    else:
        treatment_type="Standard Treatment"
        Standard_Treatment_count+=1
        patients_list_info[-1].append(treatment_type)
    print(patients_list_info)


       
print(f"Priority Treatment : {priority_count}")
print(f"Normal Treatment : {Normal_Treatment_count}")
print(f"Standard Treatment : {Standard_Treatment_count}")