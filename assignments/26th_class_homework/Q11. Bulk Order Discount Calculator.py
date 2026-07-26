def bulk_discount_total(val):
    total=0
    for i in val:
        total+=i
    if(len(val)>=5):
        total=total-total*0.1

    elif(len(val)>=10):
        total= total-total*0.5
    return total
    
# res=bulk_discount_total([500, 700, 300, 900, 600])
res=bulk_discount_total([500, 700, 300, 900, 600,7,4,2,1,1,6])
print(res)
