# portfolio_optimization.py
# Optimal Investment Strategy using Dynamic Programming (Knapsack approach)

import time

# ------------------------------#
# Stock Data (Sample Input)
# name, investment cost, expected return, risk
# ------------------------------#
stocks = [
    {"name": "Stock A", "cost": 1000, "return": 120, "risk": 5},
    {"name": "Stock B", "cost": 2000, "return": 300, "risk": 7},
    {"name": "Stock C", "cost": 1500, "return": 200, "risk": 6},
    {"name": "Stock D", "cost": 1200, "return": 150, "risk": 4},
]

budget = 4000
start_time = time.time()

n = len(stocks)

# ------------------------------#
# Dynamic Programming Table
# ------------------------------#
dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    cost = stocks[i - 1]["cost"]
    ret = stocks[i - 1]["return"]

    for b in range(budget + 1):
        if cost <= b:
            dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + ret)
        else:
            dp[i][b] = dp[i - 1][b]

# ------------------------------#
# Find Selected Stocks
# ------------------------------#
b = budget
selected_stocks = []

for i in range(n, 0, -1):
    if dp[i][b] != dp[i - 1][b]:
        selected_stocks.append(stocks[i - 1])
        b -= stocks[i - 1]["cost"]

selected_stocks.reverse()

# ------------------------------#
# Calculate Totals
# ------------------------------#
total_cost = sum(stock["cost"] for stock in selected_stocks)
total_return = sum(stock["return"] for stock in selected_stocks)
total_risk = sum(stock["risk"] for stock in selected_stocks)

end_time = time.time()

# ------------------------------#
# Display Stock Data
# ------------------------------#
print("\nSTOCK DATA")
print("------------------------------------")
print("Name\tCost\tReturn\tRisk")

for stock in stocks:
    print(f"{stock['name']}\t{stock['cost']}\t{stock['return']}\t{stock['risk']}")

print("\nAvailable Budget:", budget)

# ------------------------------#
# Display Optimal Allocation
# ------------------------------#
print("\nOPTIMAL PORTFOLIO")
print("------------------------------------")

for stock in selected_stocks:
    print(stock["name"])

print("\nTotal Investment:", total_cost)
print("Maximum Expected Return:", total_return)
print("Total Risk:", total_risk)

print("\nTime Complexity: O(n * budget)")
print("Execution Time:", round(end_time - start_time, 6), "seconds")

# ------------------------------#
# Save Output to File
# ------------------------------#
with open("portfolio_optimization_output.txt", "w") as file:
    file.write("STOCK DATA\n")
    file.write("------------------------------------\n")
    file.write("Name\tCost\tReturn\tRisk\n")

    for stock in stocks:
        file.write(f"{stock['name']}\t{stock['cost']}\t{stock['return']}\t{stock['risk']}\n")

    file.write(f"\nAvailable Budget: {budget}\n")
    file.write("\nOPTIMAL PORTFOLIO\n")
    file.write("------------------------------------\n")

    for stock in selected_stocks:
        file.write(stock["name"] + "\n")

    file.write(f"\nTotal Investment: {total_cost}\n")
    file.write(f"Maximum Expected Return: {total_return}\n")
    file.write(f"Total Risk: {total_risk}\n")

    file.write("\nTime Complexity: O(n * budget)\n")
    file.write(f"Execution Time: {round(end_time - start_time, 6)} seconds\n")

print("\nOutput saved to 'portfolio_optimization_output.txt'")