discount_list=[]
fee_list=[]
payable_fee_list=[]
name_list=[]
i=0
count=0
while True:
     
    name=input("Enter member name (or 'stop' to exit):")
    if name=="stop"or name=="exit":
        break
    name_list.append(name)
    age=int(input("Enter age: "))
    if(age >=60):
        discount=20
        discount_list.append(discount)

    elif(age <=15):
        discount=30
        discount_list.append(discount)
    plan=input("Enter plan (basic/premium/vip): ").lower();
    if(plan=="basic"):
        fee=2000;
        fee_list.append(fee)
    elif(plan=="premium"):
        fee=4000;
        fee_list.append(fee)
    elif(plan=="vip"):
        fee=7000;
        fee_list.append(fee)

    payable_fee=fee-(fee*discount/100)
    payable_fee_list.append(payable_fee)
    print(f"{name_list[i]}->Plan: {plan} |Fee:{fee_list[i]} discount: {discount_list[i]}% | Payable: {payable_fee_list[i]}")
    count+=1
    i+=1

print(f"Total members: {count}")
print("Payable fees: ",sum(payable_fee_list))