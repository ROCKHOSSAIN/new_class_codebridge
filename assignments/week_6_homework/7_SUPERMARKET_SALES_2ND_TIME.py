branch = ['Shibuya', 'Shinjuku']
category = ['Food', 'Drinks', 'Snacks']

sales = [
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

b = 0
highest_sales_amount = 0
highest_branch = ""
highest_category = ""
highest_week = 0

while b < len(sales):
    branch_total = 0
    print("\nBranch name:", branch[b])

    c = 0
    while c < len(category):
        row = category[c] + " | "

        w = 0
        while w < len(sales[b][c]):
            row += "Week " + str(w + 1) + ": " + str(sales[b][c][w]) + " | "

            branch_total += sales[b][c][w]

            if sales[b][c][w] > highest_sales_amount:
                highest_sales_amount = sales[b][c][w]
                highest_branch = branch[b]
                highest_category = category[c]
                highest_week = w + 1

            w += 1

        print(row)
        c += 1

    print("Branch Total Sales:", branch_total)
    b += 1

print("\n========================================")
print("Highest Sales Amount:", highest_sales_amount)
print("Highest Branch:", highest_branch)
print("Highest Category:", highest_category)
print("Highest Week:", highest_week)