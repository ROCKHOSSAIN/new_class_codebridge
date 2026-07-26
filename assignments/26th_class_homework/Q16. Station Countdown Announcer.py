# def countdown_announcements(n):
#     n_list=[]
#     i=n
#     while i>=0: 
#         if(i==0):
#             n_list.append("Departing now!")
#             
#         else:
#             n_list.append(f"{i} minutes to departure")



#         i-=1
#     return n_list

# res=countdown_announcements(3)
# print(res)

# or 

def countdown_announcements(minutes):
    announcements = []
    for m in range(minutes,-1,-1):
        if m == 0:
            announcements.append("Departing now!")
        else:
            announcements.append(f"{m} minutes to departure")
    return announcements