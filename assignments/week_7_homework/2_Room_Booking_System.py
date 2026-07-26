rooms = [
    ["Standard", 5000, 1],
    ["Deluxe", 8000, 1],
    ["Suite", 15000, 0],
    ["Family", 10000, 2],
    ["Executive", 20000, 1]
]
total_cost=0
print("========================================")
print("HOTEL ROOM AVAILABILITY")
print("========================================")
print()
print("No. | Type | Price/Night | Status")
print("----------------------------------------")
i=0
while i<len(rooms):
        row=str(i+1)+ " | "+ str(rooms[i][0])  + " | "+ str(rooms[i][1]) + " | " + str(rooms[i][2])
        print(row) 
        i+=1
i=0
count=0
while True:
    number=int(input("Enter room number to book ((1-5) enter 0 to exit):"))
    room_index = number - 1
    
    if(number ==0 ) :       
        break

    else:
        if(rooms[room_index][2]==0):
            print("Room not available.")
        else:
            print("Booking confirmed! Deluxe room for 3 nights")
            rooms[room_index][2]-=1
            total_cost+=rooms[i][1]*3
            count+=1
            i+=1
        

print("Total rooms booked :",count)
print("total revenue :",total_cost,"yen")
 

