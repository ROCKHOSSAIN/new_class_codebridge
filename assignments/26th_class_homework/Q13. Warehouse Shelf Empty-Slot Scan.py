def find_empty_slot(val):
    n_list=[]
    row=0
    while row<len(val):
        col=0
        while col<len(val[row]):
            if(val[row][col]==0):
                return row,col
            col+=1
        row+=1
        
    return None
res=find_empty_slot([[5, 3, 0], [2, 4, 6]])
print(res)
