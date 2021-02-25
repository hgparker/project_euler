# Method 1: 
# Recursive calculation...don't even memoize

import sys

limit = int(sys.argv[1])

repeats = {169: 3, 363601: 3, 1454: 3, 871: 2, 45361: 2, 45362: 2, 872: 2, 145: 1, 1:1, 2:1, 40585: 1}
facs = [1]
while len(facs) <= 9:
  facs.append(facs[-1] * len(facs))

def calculate(n, depth):
  if n in repeats: return repeats[n] + depth
  sum = 0
  q = n
  while q > 0:
    sum += facs[q % 10]
    q //= 10
  return calculate(sum, depth+1)

count = 0
for k in range(1, limit):
  if calculate(k, 0) == 60:
    count += 1

print(count)