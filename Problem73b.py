# Method 2 
# Sieve the prime factors <= d
# Use PIE-recursive calculator for each individual d

import sys
import math

def PIE_recursive(primes, primeIndex, maxExcludedNumerator, maxIncludedNumerator, multiplier):
  multiplier *= primes[primeIndex]
  base = maxIncludedNumerator // multiplier - maxExcludedNumerator // multiplier
  for k in range(primeIndex+1, len(primes)):
    base -= PIE_recursive(primes, k, maxExcludedNumerator, maxIncludedNumerator, multiplier)
  return base

d = int(sys.argv[1])

sieve = [[] for k in range(d+1)]
for k in range(2, d+1):
  if len(sieve[k]) == 0:
    for p in range(k, d+1, k):
      sieve[p].append(k)

num = 0
for k in range(5, d+1):
  maxExcludedNumerator = math.floor(k/3)
  maxIncludedNumerator = math.ceil(k/2) - 1  
  deltaNum = maxIncludedNumerator - maxExcludedNumerator
  for primeIndex in range(len(sieve[k])):
    deltaNum -= PIE_recursive(sieve[k], primeIndex, maxExcludedNumerator, maxIncludedNumerator, 1)
  num += deltaNum

print(num)