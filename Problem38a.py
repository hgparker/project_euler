# Method 1
# control on number of starting digits of seed
# figure out acceptable combinations of seeDigits & seedDigits+1 to get to 9
# use combination starting-points to get lower and upper bounds
# try all the seeds

import math
import functools as ft

def isPandigital(nums):
  digits = 0
  for num in nums:
    while num > 0:
      digits |= 1 << (num % 10)
      num //= 10
  return digits == 1022

maxFound = -math.inf
for seedDigits in range(1, 5):
  for a in range(1, (9 // seedDigits) + 1):
    if (9 - a*seedDigits) % (seedDigits+1) != 0: continue
    b = (9 - a*seedDigits) // (seedDigits + 1)
    seedStart = 10 ** (seedDigits-1) if b == 0 else math.ceil((10 ** seedDigits) / (a+1)) 
    seedEnd = math.ceil((10 ** seedDigits) / a)
    for seed in range(seedStart, seedEnd):
      nums = [k*seed for k in range(1, a + b + 1)]
      if isPandigital(nums):
        maxFound = max(maxFound, int(ft.reduce(lambda x,y: str(x) + str(y), nums)))

print(maxFound)