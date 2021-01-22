#Method 1 : knapsack

import sys

totalAmount = int(sys.argv[1])

coins = [2, 5, 10, 20, 50, 100, 200]

numberWays = [1] * (totalAmount + 1)

for coin in coins:
  for k in range(coin, totalAmount+1):
    numberWays[k] += numberWays[k-coin]

print(numberWays[totalAmount])