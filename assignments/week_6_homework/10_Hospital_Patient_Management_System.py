patients_list = []
severity_list = []
patients_age = []
treatment_type_list=[]
priority_count=0
Normal_Treatment_count=0
Standard_Treatment_count=0
while True:
    patient_name=input("Enter patient name (or 'done'): ")
    if patient_name=="done":
        i=0
        while i<len(patients_list):
            print(f"{patients_list[i][0]}|  Age: {patients_age[i]} | Severity: {severity_list[i]} -> {treatment_type_list[i]}")
            i+=1
        break

    patient_name = patient_name.title()
    patients_list.append([patient_name])
    age=int(input("Enter age: "))#
    patients_age.append(age)
    severity=int(input("Enter severity (1-10): "))
    severity_list.append(severity)
    if age>=60 or severity>=7:
       treatment_type="Priority Treatment" 
       priority_count+=1
       treatment_type_list.append(treatment_type)
    elif age>=18 or severity>=4:
        treatment_type="Normal Treatment"
        Normal_Treatment_count+=1
        treatment_type_list.append(treatment_type)
    else:
        treatment_type="Standard Treatment"
        Standard_Treatment_count+=1
        treatment_type_list.append(treatment_type)


       
    # print(f"Patient added: {patient_name}, Age: {age}, Severity: {severity}")
print(f"Priority Treatment : {priority_count}")
print(f"Normal Treatment : {Normal_Treatment_count}")
print(f"Standard Treatment : {Standard_Treatment_count}")