from collections import Counter
from itertools import permutations

fourDigitPrimes = []
sieve = [True] * 10000

for k in range(2, 10000):
  if sieve[k]:
    if k > 1000: fourDigitPrimes.append(k)
    for p in range(k*2, 10000, k):
      sieve[p] = False

def digitize(num):
  return [num // 1000, (num // 100) % 10, (num // 10) % 10, num % 10]

def detectThird(second, third):
  if third >= 10000: return False
  if not sieve[third]: return False
  return Counter(digitize(second)) == Counter(digitize(third))

# print(detectThird(4817, 8147))
doubles = set()

for prime in fourDigitPrimes:
  for a, b, c, d in permutations(digitize(prime)):
    second = 1000*a+100*b+10*c+d
    if second <= prime or not sieve[second]: continue
    if (prime, second) not in doubles and detectThird(second, 2*second - prime):
      doubles.add((prime, second))

for first, second in doubles:
  print(first, second, 2*second-first)
