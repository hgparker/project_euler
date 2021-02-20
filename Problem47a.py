# Method 1
# Sieve for number of prime factors and find first

import sys
n = int(sys.argv[1])

last = 0
numInRow = 0
sieve = [0] * 100
primes = set()
k = 2
while True:
  if k >= len(sieve):
    sieve += [0] * len(sieve)
    for p in primes:
      start = ((len(sieve) // 2) // p) * p
      for multiple in range(start, len(sieve), p):
        sieve[multiple] += 1
  if sieve[k] == 0:
    primes.add(k)
    for multiple in range(k, len(sieve), k):
      sieve[multiple] += 1
  elif sieve[k] == n:
    if last == k-1:
      numInRow += 1
      last = k
      if numInRow == n:
        print(k-numInRow+1)
        break
    else:
      numInRow = 1
      last = k      
  k += 1
