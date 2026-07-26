username=input("Enter your username: ")
if len(username) >= 5 and username.isalpha():
    print("Valid username")
elif len(username) < 5 or not username.isalpha():
    print("Invalid username")
