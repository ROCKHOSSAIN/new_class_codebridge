def place_item(warehouse, floor, shelf, slot, item_id):
    warehouse[floor][shelf][slot]=item_id
    return warehouse[floor][shelf][slot]
def count_floor_items(warehouse, floor):
    count=0
    i=0
    while i<len(warehouse[floor]):
        j=0
        while j<len(warehouse[floor][i]):
            if(warehouse[floor][i][j]!=None):
                count+=1
            j+=1
        i+=1
    return count
        

    
    
warehouse = [
    # floor 1
    [ [None, None],[101, None]],
    # floor 2
    [[None, 202], [None, None]]
]
res=place_item(warehouse, 0, 0, 1, 305)
print(res)
res1=count_floor_items(warehouse, 0)
print(res1)