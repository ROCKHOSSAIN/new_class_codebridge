member_status=input("Are you a member?(yes/no): ").lower()
if member_status=="yes":
    bill_amount=int(input("Enter  bill amount: "))
    discount=bill_amount*0.1
elif member_status=="no":
    bill_amount=int(input("Enter your bill amount: "))
    discount=0

print(f"final bill amount is: {bill_amount-discount}")    