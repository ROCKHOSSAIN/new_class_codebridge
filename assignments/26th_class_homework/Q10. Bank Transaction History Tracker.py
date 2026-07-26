start_balance=500
transactions = [200, -100, -700, 50, -1000]
n_list=[]
for index,i in enumerate(transactions):
    if(i>0):
        start_balance+=i
    elif(i<0):
        if(start_balance+i>0):
            start_balance+=i
        elif(start_balance+i<0):
            n_list.append(index)
            continue
print((start_balance,n_list))
