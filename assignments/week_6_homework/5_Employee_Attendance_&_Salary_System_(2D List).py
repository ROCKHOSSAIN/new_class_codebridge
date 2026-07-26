employees = [
    ["Aiko yamamoto", 28, 2000],
    ["Kenji mori", 18, 1500],
    ["Hana Sato", 22, 1800],
    ["Riku Tanaka", 26, 2500]
]
salary=[]
status=[]
i=0
print("=========================")
print("MONTHLY PAYROLL REPORT")
print("=========================")
print("Name | Days | Daily Wage | Salary | Status")
print("------------------------------")
while i<len(employees):
    total_salary=employees[i][1]*employees[i][2]
    if(employees[i][1] < 20 ):
        salary.append(total_salary-(total_salary*0.1))  # Assuming 10% deduction for employees under 20
        status.append("Deduced")
    elif(employees[i][1] >= 26):
        
        salary.append(total_salary+(total_salary*0.05))  # Assuming 10% bonus for employees 26 and older
        status.append("Bonus")
    else:
        salary.append(total_salary)
        status.append("Standard")
   
    print(f"{employees[i][0].title()} | {employees[i][1]} | {employees[i][2]} | {salary[i]} | {status[i]}")
    i+=1
print("------------------------------")


print(f"Total Payroll : {sum(salary)}")
