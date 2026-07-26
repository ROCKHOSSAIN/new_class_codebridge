email = input("Enter your email: ")
if "@" in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")