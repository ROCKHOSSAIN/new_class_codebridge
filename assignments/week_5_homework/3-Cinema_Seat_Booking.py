seats = [10, 11, 12, 13, 14, 15, 16]
print("First seat:", seats[0])
print("Last seat:", seats[-1])
booked_seats= seats[2:5]
if(len(booked_seats) == 3):
    print(f"Booked seats: {booked_seats} ")
    print("Booking confirmed for 3 seats!")
else:
    print("Booking failed. Not enough seats available.")