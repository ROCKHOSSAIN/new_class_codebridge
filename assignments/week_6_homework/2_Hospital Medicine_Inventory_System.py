medicine_list=[]
medicine_quantity =[]
medicine_unit = []
total_price_list=[]
status = []
max_price=[]
while True:
    medicine_name = input("Enter medicine name (or 'done') : ").title()
    if medicine_name == "Done":
        break

    quantity = int(input("Enter Quantity:" ))
       
    if(quantity >= 100):
             status.append("Sufficient")
    elif(quantity >= 50):
             status.append("low")
    else:
             status.append("Critical")

    
    unit_price=float(input("Enter unit price: "))
    total_price = quantity * unit_price
    medicine_list.append(medicine_name)
    medicine_quantity.append(quantity)
    medicine_unit.append(unit_price)
    total_price_list.append(total_price)
    # print(f"status{status}")

    
print("==========================================================")
print("PHARMACY INVENTORY REPORT");
print("==========================================================")
print("Medicine  | Qty  | Unit Price | Total Value |Status")
print("----------------------------------------------------------")
i=0
while i<len(medicine_list):
   print(f"{medicine_list[i]} | {medicine_quantity[i]} | {medicine_unit[i]} | {total_price_list[i]} | {status[i]}")
   i=i+1;
print("----------------------------------------------------------")
max_value = max(total_price_list)
max_value_index = total_price_list.index(max_value)
print(f"Highest value stock: {medicine_list[max_value_index]}  ({max_value}) yen")