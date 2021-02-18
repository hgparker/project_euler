# Method
# co-generate primes and composites using sieve
# scan by squares, fail fast, and use hash
# note that better to scan by squares rather than primes b/c x/log(x) > x/sqrt(x)

from math import sqrt, floor
from bisect import bisect_left

sieve = [True] * 100
primes = set()
k = 2
while True:
  if k >= len(sieve):
    sieve += [True] * len(sieve)
    for p in primes:
      start = ((len(sieve) // 2) // p) * p
      for multiple in range(start, len(sieve), p):
        sieve[multiple] = False
  if sieve[k]:
    primes.add(k)
    for multiple in range(2*k, len(sieve), k):
      sieve[multiple] = False
  elif k % 2 == 1:
    square = 1
    notFound = True
    while k - 2*square*square > 1 and notFound:
      if k-2*square*square in primes: notFound = False
      square += 1
    if notFound:
      print(k)
      break
  k += 1