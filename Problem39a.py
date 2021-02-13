# Method 1
# Use Euclid's formula to generate all primitive triples
# Then sieve upward from primitives and get max

import sys
import math

maxPerimeter = int(sys.argv[1])
primitiveCount = {}

m = 2
count = 0
while 2*m * (m+1) <= maxPerimeter:
  if m % 2 == 0:
    n = 1
    increment = 1
  else:
    n = 2
    increment = 2
  while n < m and 2*m*(m+n) <= maxPerimeter:
    if math.gcd(m, n) == 1:
      primitiveCount[2 * (m ** 2) + 2*m*n] = primitiveCount.get(2 * (m ** 2) + 2*m*n, 0) + 1
      count += 1
    n += increment
  m += 1

print("begin second part")

allCount = [0] * (maxPerimeter+1)
for primitive in primitiveCount:
  for multiple in range(primitive, maxPerimeter+1, primitive): 
    allCount[multiple] += primitiveCount[primitive]

bestPerimeter = 0
for k in range(maxPerimeter+1):
  if allCount[k] > allCount[bestPerimeter]:
    bestPerimeter = k

print("best perimeter", bestPerimeter, allCount[bestPerimeter])