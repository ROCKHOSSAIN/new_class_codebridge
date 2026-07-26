def rating_label(n):
    # if n==1 or n==2:
    if n in (1,2):
        return "beginner"
    elif n==3:
        return "Intermediate"
    elif n==4:
        return "advanced"
    elif n==5:
        return "expert"
    else:
        return "Invalid"


print(rating_label(4))
print(rating_label(1))
print(rating_label(9))
