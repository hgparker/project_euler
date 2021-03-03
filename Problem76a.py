# Method 1
# Use Euler's pentagonal number theorem

from functools import cache

# get kth pentagonal number
def pentagonal(k):
  return k * (3*k - 1) // 2

@cache
def partition(n):
  if n == 0: return 1
  sum = 0
  k = 1
  while n - pentagonal(k) >= 0:
    if k % 2 == 0:
      sum -= partition(n-pentagonal(k))
    else:
      sum += partition(n-pentagonal(k))
    k += 1
  k = -1
  while n - pentagonal(k) >= 0:
    if k % 2 == 0:
      sum -= partition(n - pentagonal(k))
    else:
      sum += partition(n - pentagonal(k))
    k -= 1
  return sum

print(partition(100)-1)