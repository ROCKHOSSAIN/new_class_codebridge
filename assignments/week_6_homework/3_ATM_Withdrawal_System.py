intial_balance = 50000

print(f"Balance: {intial_balance}")
while True:
    withdraw = int(input("Enter withdrawal amount (or 0 to exit): "))
    if(withdraw==0):
        print(f"Thank you! Final balance: {intial_balance}")
        break
    if(withdraw > intial_balance):
        print("Insufficient funds")
    else:
        intial_balance -= withdraw
        print(f"Withdrawal successful. Remaining balance: {intial_balance}")

