names=[]
prices=[]
while True:
    
    product_name=input("Enter product (or 'done' to finish): ")
   
    if(product_name=="done"):
        break

    names.append(product_name)
    product_price=int(input("Enter price: "))
    prices.append(product_price)

print("--- Your Receipt ---")
    
i=0
while i < len(names):

    print(f"{names[i]} : {prices[i]}")

    i += 1

print(f"Total items: {len(names)}")
print(f"Total bill: {sum(prices)}")