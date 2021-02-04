# Method 1
# Get primes < n by sieving and check each one

import sys

n = int(sys.argv[1])

sieve = [True] * n
primes = set([2])

def containsEvenDigit(q):
  while q > 0:
    if q % 2 == 0:
      return True
    q //= 10
  return False

def rightshift(q, numdigits):
  digit = q % 10
  return (q // 10) + digit * (10 ** (numdigits-1))

def countDigits(q):
  numDigits = 1
  while q >= 10:
    q //= 10
    numDigits += 1
  return numDigits

def cycle(prime, originalPrime, numDigits):
  if prime == originalPrime:
    solutions.add(originalPrime)
    return 1
  
  if not prime in primes:
    return 0
  
  ret = cycle(rightshift(prime, numDigits), originalPrime, numDigits)
  if ret == 0:
    return ret
  else:
    solutions.add(prime)
    return ret + 1

for k in range(2, n):
  if not sieve[k]:
    continue
  if not containsEvenDigit(k): primes.add(k)
  for m in range(k, n, k):
    sieve[m] = False

solutions = set()
numSolutions = 0
for prime in list(primes):
  if prime not in solutions:
    numDigits = countDigits(prime)
    numSolutions += cycle(rightshift(prime, numDigits), prime, numDigits)

print(numSolutions)