branch_name=['Shibuya','Shinjuku']
category=['Food', 'Drinks', 'Snacks']

predefined_sales_amount=[ 
[
        [120000, 135000, 118000, 142000], 
        [85000, 90000, 88000, 95000],
        [45000, 50000, 47000, 53000]
    ],
    [
        [155000, 160000, 148000, 170000],
        [92000, 98000, 94000, 102000],
        [60000, 65000, 58000, 70000]
    ]
]

print("========================================")
print("SUPERMARKET SALES REPORT")
print("========================================")
b=0
highest_sales_amount = 0
highest_branch = ""
highest_category = ""
highest_week = 0
while b < len(branch_name):
     branch_total=0
     print("Branch:",branch_name[b])

     c=0
     while c<len(category):
          row = category[c]+" | "

          w=0
          while w<len(predefined_sales_amount[b][c]):
               row = row+"week "+str(w+1)+": "+ str(predefined_sales_amount[b][c][w]) + " | "
               branch_total += predefined_sales_amount[b][c][w]

               if predefined_sales_amount[b][c][w] > highest_sales_amount:
                    highest_sales_amount = predefined_sales_amount[b][c][w]
                    highest_branch = branch_name[b]
                    highest_category = category[c]
                    highest_week = w+1

               w += 1
          print(row)
          c += 1

     print("branch total sales:", branch_total)
     b += 1
print("highest sales amount: ",highest_sales_amount)
print("highest branch: ",highest_branch)
print("highest category: ",highest_category)
print("highest week: ",highest_week)




