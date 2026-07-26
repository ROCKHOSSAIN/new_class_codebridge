username = "admin"
password = "12345"
OTP = "9999"

username = input("Enter username: ")
password = input("Enter password: ")
OTP = input("Enter OTP: ")

if(username == "admin"):
    if(password == "12345"):
        if(OTP == "9999"):
            print("Login approved!")
        else:
            print("Invalid OTP.")
    else:
        print("Wrong password.")
else:
    print("Invalid Username.")
