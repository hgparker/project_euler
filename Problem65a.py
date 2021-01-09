# Method1: use convergence recurrence and e's pcf to get 100th and then sum numerator

import sys

def getPCFe(k):
  if k % 3 != 2:
    return 1
  else:
    return 2 * (k+1) // 3

def getConvergentNumerator(k):
  aPenult = 1
  aUlt = 2

  for k in range(1, k):
    aNew = getPCFe(k) * aUlt + aPenult
    aPenult = aUlt
    aUlt = aNew
  
  return aUlt

def sumDigits(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

print(sumDigits(getConvergentNumerator(int(sys.argv[1]))))




