vehicle = input("Enter vehicle type (car/bike/truck): ").lower()
parking_hours = int(input("Enter parking hours: "))
if vehicle == "car":
    fees = 300 
elif vehicle == "bike":
    fees = 100
elif vehicle == "truck":
    fees = 500
else:
    print("Invalid vehicle type")
    fees = 0

print(f"Parking fees: {fees * parking_hours} yen")