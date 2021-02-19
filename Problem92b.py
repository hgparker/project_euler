# Method 2: DFS w/ memoization over multiset 

import sys
from itertools import combinations_with_replacement
from functools import reduce

numDigits = int(sys.argv[1])

chainTerminus = {}
chainTerminus[(numDigits, 0, 0, 0, 0, 0, 0, 0, 0, 0)] = 0
chainTerminus[(numDigits-1, 1, 0, 0, 0, 0, 0, 0, 0, 0)] = 1
chainTerminus[(numDigits-2, 0, 0, 0, 0, 0, 0, 0, 1, 1)] = 89

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
facs = [1]
while len(facs) < numDigits + 1:
  facs.append(facs[-1] * len(facs))

def digitize(n):
  digitCount = [0] * 10
  for k in range(numDigits):
    digitCount[n % 10] += 1
    n //= 10
  return tuple(digitCount)

def digitize2(t):
  digitCount = [0] * 10
  for digit in t:
    digitCount[digit] += 1
  return tuple(digitCount)

def calculate(n):
  if n in chainTerminus: return chainTerminus[n]
  sum = 0
  for a, b in zip(n, squares):
    sum += a*b
  chainTerminus[n] = calculate(digitize(sum))  
  return chainTerminus[n]

count = 0
for k in combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numDigits):
  m = digitize2(k)
  if calculate(m) == 89:
    divider = reduce(lambda a, b: a*b, map(lambda x: facs[x], m))
    count += facs[numDigits] // divider

print(count)