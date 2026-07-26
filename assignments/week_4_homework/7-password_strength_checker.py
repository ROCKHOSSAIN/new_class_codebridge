password=input("Enter your password: ")
if len(password)>=8 and any(char.isdigit() for char in password):
    print("Strong password")
else :
    print("Weak password")