# Method 2
# Don't sieve, just try only odd digit permutations for primality

import itertools as it

primes = {}
def isPrime(q):
  if q in primes:
    return primes[q]

  if q < 2:
    primes[q] = False
    return False

  candidateFactor = 2
  while candidateFactor * candidateFactor <= q:
    if q % candidateFactor == 0:
      primes[q] = False
      return False
    candidateFactor += 1
  primes[q] = True
  return True

def rightshift(q, numdigits):
  digit = q % 10
  return (q // 10) + digit * (10 ** (numdigits-1))

def cycle(number, originalNumber, numDigits):
  if number == originalNumber:
    solutions.add(originalNumber)
    return 1
  
  if not isPrime(number):
    return 0
  
  ret = cycle(rightshift(number, numDigits), originalNumber, numDigits)
  if ret == 0:
    return ret
  else:
    solutions.add(number)
    return ret + 1

oddDigits = [1,3,7,9]
numSolutions = 2 # for 2 and 5
solutions = set()
tens = [1]

for numDigits in range(1, 7):
  for digitPermutation in it.product(oddDigits, repeat=numDigits):
    number = sum(map(lambda k: digitPermutation[k]*tens[k], range(numDigits)))
    if isPrime(number) and not number in solutions:
      numSolutions += cycle(rightshift(number, numDigits), number, numDigits)
  tens = list(map(lambda x: x*10, tens))
  tens.append(1)

print(numSolutions)