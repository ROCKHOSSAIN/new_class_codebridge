def fare_announcements(n):
    n_list=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            n_list.append("rapidexpress")
        elif i==3:
            n_list.append("local")
        elif i==5:
            n_list.append("express")
        
        elif i!=3 and i!=5 or i%3!=0 and i%5!=0:
            n_list.append(i)
        
    return n_list
result = fare_announcements(15)
print(result)
