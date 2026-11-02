# Take number of items
n = int(input("Enter number of items: "))
items = []

# Take profit and weight of each item
for i in range(n):
    profit = float(input(f"Enter profit of item {i + 1}: "))
    weight = float(input(f"Enter weight of item {i + 1}: "))

    ratio = profit / weight
    items.append((ratio, profit, weight))

# Take capacity of knapsack
capacity = float(input("Enter capacity of knapsack: "))

# Sort items according to profit/weight ratio in descending order
items.sort(reverse=True)

total_profit = 0

# Select items greedily
for ratio, profit, weight in items:

    if capacity >= weight:
        # Take complete item
        capacity = capacity - weight
        total_profit = total_profit + profit

    else:
        # Take fractional part of item
        fraction = capacity / weight
        total_profit = total_profit + (profit * fraction)
        capacity = 0
        break

print("\nMaximum Profit =", total_profit)
