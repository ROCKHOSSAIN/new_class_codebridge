def sales_summary(amount):
    total=sum(amount)
    avg=total/len(amount)
    count=0
    for s in amount:
        if(avg>s):
            count+=1
    return total,count
res=sales_summary([12000, 8000, 15000, 9000])
print(res)
