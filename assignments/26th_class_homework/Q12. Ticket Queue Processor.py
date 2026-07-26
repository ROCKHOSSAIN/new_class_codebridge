def serve_queue(val):
    # i=0
    # n_list=[]
    # while i<len(val):
    #     if(val[i]!="END"):
    #         n_list.append(val[i])
    #     else:
    #         break;
    #     i+=1
    # return n_list
    served=[]
    q=val[:]
    while q:
        ticket=q.pop(0)
        if ticket=="END":
          break;
        served.append(ticket)
    return served
res=serve_queue([101, 102, 103, "END", 104])
print(res)