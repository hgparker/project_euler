# Method 1
# Use formulas for diagonals, test primality and keep running average

import sys

percentage = int(sys.argv[1])

def isPrime(n):
  if n == 2 or n == 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  k1 = 5
  k2 = 7
  while k1 * k1 <= n:
    if n % k1 == 0 or n % k2 == 0:
      return False
    k1 += 6
    k2 += 6
  return True

n = 1
numPrimes = 0
while True:
  NW = 4*n*n + 1
  SW = NW + 2*n
  NE = NW - 2*n

  numPrimes += 1 if isPrime(NW) else 0
  numPrimes += 1 if isPrime(SW) else 0
  numPrimes += 1 if isPrime(NE) else 0
  if numPrimes * 100 < percentage * (4 * n + 1):
    print(2*n+1)
    break
  n += 1