salary = float(input("Enter salary: "))

if salary > 1000000:
    tax_rate = 0.30
elif salary > 500000:
    tax_rate = 0.10
else:
    tax_rate = 0.0

tax_amount = salary * tax_rate
print(f"Tax: {tax_amount}")