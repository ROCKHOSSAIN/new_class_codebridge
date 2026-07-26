age = int(input("Enter age: "))
level = int(input("Enter emergency level: "))

if age >= 60 or level >= 7:
    print("Priority Treatment")
elif age >= 18 and level >= 4:
    print("Normal Treatment")
else:
    print("Standard Queue")