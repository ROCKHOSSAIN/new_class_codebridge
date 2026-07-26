def second_highest(scores):
    updated=set(scores)
    sort=sorted(updated)
    print(sort)
    if(len(sort)>=2):
        second_unique=sort[-2]
    else:
        return None
    return second_unique

    

scores=[88, 92, 92, 75, 100]
# scores=[100]
res=second_highest(scores)
print(res)