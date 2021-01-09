# Method1 ...just get period by using periodic continued fraction surd recurrence
# Count the odd ones

import math
import sys

def getPeriodLength(n):
  m = 0
  d = 1
  a = initialA = math.floor(math.sqrt(n))
  periodLength = 0

  while a != 2*initialA:
    m = d*a - m
    d = (n - m * m) / d
    a = math.floor((initialA+m) / d)
    periodLength += 1

  return periodLength

N = int(sys.argv[1])
numOddPeriods = 0

nextSquareRoot = 2
nextSquare = 4
for k in range(2, N+1):
  if k != nextSquare:
    numOddPeriods += 1 if getPeriodLength(k) % 2 == 1 else 0
  else:
    nextSquare += 2*nextSquareRoot + 1
    nextSquareRoot += 1

print(numOddPeriods)