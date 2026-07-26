product_stock=[]

while True:
    product_name=input("Enter product name (or 'done'):")
    if product_name=="done":
        print("You have not entry any products")
        break
    category=input("Enter category:")
    quantity=int(input("Enter quantity:"))
    unit_price=float(input("Enter unit price:"))
    product_stock.append([product_name,category,quantity,unit_price])


print("========================================")
print("WAREHOUSE INVENTORY REPORT")
print("========================================")

print("Product | Category  | Qty  | Unit Price | Total Value |Stock")
print("----------------------------------------------------------")

i=0
highest_price=0
highest_price_product=""
stock=""
while i<len(product_stock):
    if(product_stock[i][2]>=100):
        stock="high"
    elif(product_stock[i][2]>=50):
        stock="medium"
    elif(product_stock[i][2]<50):
        stock="low"


    total_price=product_stock[i][2]*product_stock[i][3]
    if(total_price>highest_price):
        highest_price=total_price
        highest_price_product=product_stock[i][0]

    print(f"{product_stock[i][0]} | {product_stock[i][1]} | {product_stock[i][2]} | {product_stock[i][3]} | {total_price}  | {stock}")

    i+=1
print("----------------------------------------------------------")
print(f"Highest value product:{highest_price_product} ({highest_price}) yen")
