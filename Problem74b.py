# Method 2: 
# Recursive calculation, but this time, memoize

import sys

limit = int(sys.argv[1])

nonRepeat = {169: 3, 363601: 3, 1454: 3, 871: 2, 45361: 2, 45362: 2, 872: 2, 145: 1, 1:1, 2:1, 40585: 1}
facs = [1]
while len(facs) <= 9:
  facs.append(facs[-1] * len(facs))

def calculate(n):
  if n in nonRepeat: return nonRepeat[n]
  sum = 0
  q = n
  while q > 0:
    sum += facs[q % 10]
    q //= 10
  nonRepeat[n] = calculate(sum) + 1
  return nonRepeat[n]

count = 0
for k in range(1, limit):
  if calculate(k) == 60:
    count += 1

print(count)