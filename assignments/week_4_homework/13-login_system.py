username = input("Enter username: ")
password = input("Enter password: ")
if username =="admin":
    if password =="12345":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid Username")