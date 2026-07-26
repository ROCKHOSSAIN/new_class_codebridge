salary = float(input("Enter salary: "))
experience = int(input("Enter experience: "))

if salary >= 300000 and experience >= 2:
    print("Loan Approved")
elif salary < 300000:
    print("Salary requirement not met")
else:
    print("Experience requirement not met")