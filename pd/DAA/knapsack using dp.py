
# 0-1 Knapsack using Dynamic Programming

n = int(input("Enter number of items: "))

weight = []
profit = []

for i in range(n):
    p = int(input("Enter profit: "))
    w = int(input("Enter weight: "))
    profit.append(p)
    weight.append(w)

capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for j in range(capacity + 1):

        if weight[i - 1] <= j:
            dp[i][j] = max(
                profit[i - 1] + dp[i - 1][j - weight[i - 1]],
                dp[i - 1][j]
            )
        else:
            dp[i][j] = dp[i - 1][j]

print("\nMaximum Profit =", dp[n][capacity])
