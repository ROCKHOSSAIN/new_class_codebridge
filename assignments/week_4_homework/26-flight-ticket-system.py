nationality = input("Enter nationality: ")
passport = input("Is passport valid? ").lower()

if passport == "yes":
    print("Ticket Booking Allowed")
else:
    print("Ticket Booking Denied")