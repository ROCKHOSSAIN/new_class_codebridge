attendance = float(input("Enter attendance: "))
assignment_submitted = input("Assignment submitted? ").lower()

if attendance >= 75 and assignment_submitted == "yes":
    print("Eligible for final exam")
elif attendance < 75:
    print("Not eligible (low attendance)")
else:
    print("Not eligible (missing assignment)")