def convert_and_print(amount,rate):
    s=int(amount.replace(",",""))
    rate=float(rate)*s

    value=rate>1000
    return s,rate,value

    # print(s)


amount,rate=input().split()


result=convert_and_print(amount,rate)

print(result)