def find_seat(seating,name):
    print(seating,name)
    i=0
    list_append=[]
    while i<len(seating):
        j=0
        while j<len(seating[i]):
            if(seating[i][j]==name):
                list_append.append(i)
                list_append.append(j)
            j+=1
            print(i,j)
        i+=1
        
        
    return list_append


    


seating = [
    ["Aisha", "Rafi", None],
    [None, "Tanvir", "Nadia"]
]
res=find_seat(seating, "Nadia")
print(res)