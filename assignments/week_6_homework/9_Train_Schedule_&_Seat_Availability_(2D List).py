trains = ["Nozomi", "Hikari", "Kodama", "Sakura"]

seat_classes = ["Green", "Reserved", "Unreserved", "Standing", "Disabled"]

seats = [
    [12, 45, 0, 0, 3],
    [0, 10, 22, 15, 2],
    [5, 0, 30, 40, 0],
    [8, 20, 18, 0, 5]
        ]
i=0
while True:
    train = int(input("Enter train number to check (0-3, or -1 to exit): "))
    if train == -1:
        print("Goodbye!")
        break
    print(f"--- {trains[train]} Seat Status ---")
    i=0
    while i<len(seat_classes):
        if seats[train][i] > 0:
            print(f"{seat_classes[i]}: Available ({seats[train][i]} seats)")
        else:
            print(f"{seat_classes[i]}: Full")
        i+=1