age = int(input("Enter age: "))

if 0 <= age <= 12:
    fare = 150
elif 12 < age <= 17:
    fare = 300
elif 17 < age <= 59:
    fare = 500
else:
    fare = 200

print(f"Bus fare: {fare} yen")