product_quantities= [0, 5, 12, 0, 3]
print(f"Total products: {len(product_quantities)}")
maximum = max(product_quantities)
minimum = min(product_quantities)
print(f"Maximum Stock: {maximum}")
print(f"Minimum stock: {minimum}")
product_quantities[0] = 8
print(f"Updated stock: {product_quantities}")