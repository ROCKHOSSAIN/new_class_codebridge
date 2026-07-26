member_ship_status = input("Are you a member? (yes/no): ")
amount = float(input("Enter amount: "))
if member_ship_status == "yes":
    if amount >= 20000:
        discount = amount * 0.03
    elif amount >= 10000:
        discount = amount * 0.02
    elif amount <10000:
        discount = amount * 0.01
else:
    print("You are not eligible for a discount.")
    discount = 0

print(f"Your discount is: {amount - discount:.1f}")

