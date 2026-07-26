gpa = float(input("Enter GPA: "))
IELTS = float(input("Enter IELTS: "))

if gpa >= 3.5 and IELTS >= 6.5:
    print("Eligible for admission")
elif gpa < 3.5:
    print("GPA requirement not met")
else:
    print("IELTS requirement not met")