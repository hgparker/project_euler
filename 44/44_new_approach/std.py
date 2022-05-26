
from math import gcd

max_C = 40

def allPhi(n):
  sieve = [k for k in range(n)]
  for k in range(2, n):
    if sieve[k] == k:
      for p in range(k, n, k):
        sieve[p] *= k-1
        sieve[p] //= k
  return sieve

sieve = allPhi(max_C+1)

def inv(number, base):
  return pow(number, sieve[base]-1, base)

def apt(s, t):
  s_prime, t_prime = inv(s, t), inv(s-t, s)
  a = s*t -s_prime*t_prime
  b = s*s_prime + t*t_prime
  c = s*t + s_prime*t_prime
  return a, b, c

for s in range(1, max_C+1):
  for t in range(1, max_C+1):
    if s*t >= max_C: break
    if gcd(s, t) != 1: continue
    a, b, c = apt(s, t)
    if b < a or c >= max_C: continue
    print(a, b, c, a**2 + b**2 - c**2 == 1)