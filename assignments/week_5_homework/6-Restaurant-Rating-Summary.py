ratings = [3.8, 4.5, 2.9, 4.8, 4.1]
highest = max(ratings)
lowest = min(ratings)
MintoMax = sorted(ratings)
ReverseOrder = sorted(MintoMax, reverse=True)
print(ReverseOrder)
toprated = ReverseOrder[0]
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Ranked: {ReverseOrder}")
if(toprated >= 4.5):
    print("Top restaurant qualifies for Featured badge!")
else:
    print("No featured badge this week")