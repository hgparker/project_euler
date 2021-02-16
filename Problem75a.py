# Method 1
# Generate all primitives and get the multiples
# if we already have >= 1 solution at a primitive, don't bother to handle the multiples since they're already excluded

import sys
import math

maxPerimeter = int(sys.argv[1])

numSolutions = {}

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
      p = 2 * (m ** 2) + 2*m*n
      if numSolutions.get(p, 0) <= 1:
        for multiple in range(p, maxPerimeter+1, p):
          numSolutions[multiple] = numSolutions.get(multiple, 0) + 1
    n += increment
  m += 1

print(len(list(filter(lambda s: numSolutions[s] == 1, numSolutions))))
