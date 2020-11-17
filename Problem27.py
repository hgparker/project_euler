import sys

primeCache = {}

def isPrime(n):
  if n in primeCache:
    return primeCache[n]
  else:
    primeCache[n] = isPrimeCalc(n)
    return primeCache[n]
  
def isPrimeCalc(n):

  if n < 2:
    return False

  if n == 2 or n == 3:
    return True

  if n % 2 == 0 or n % 3 == 0:
    return False
  
  candidateDivisor1 = 5
  candidateDivisor2 = 7

  while candidateDivisor1 * candidateDivisor1 <= n:
    if n % candidateDivisor1 == 0:
      return False
    if n % candidateDivisor2 == 0:
      return False
    candidateDivisor1 += 6
    candidateDivisor2 += 6

  return True

c = int(sys.argv[1])
maxPrimeStreak = 0

if c % 2 == 1:
  c -= 1

for a in range(-c+1, c, 2):
  for b in range(max(-c+1, -a, maxPrimeStreak + a), c, 2):
    
    if not isPrime(b):
      continue

    n = 0
    while isPrime(n*n + a*n + b):
      n += 1
    if n > maxPrimeStreak:
      coefficients = [a,b]
      maxPrimeStreak = n

print([maxPrimeStreak,coefficients])