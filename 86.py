import sys
from itertools import product
from functools import reduce
from math import gcd
from math import sqrt

###

def get_primes_lpf(N):
  """
  (1) Returns list of all primes <= N as well as least prime factor of all <= N
  (2) O(N) 
  """
  lpf = [0] * (N+1)
  primes = []
  for k in range(2, N+1):
    if lpf[k] == 0:
      lpf[k] = k
      primes.append(k)

    q = 0
    while k * primes[q] <= N:
      lpf[k*primes[q]] = primes[q]
      if primes[q] == lpf[k]:
        break
      q += 1
  return primes, lpf

def get_lpf(N):
  return get_primes_lpf(N)[1]

def get_prime_factorization(lpf, n):
  """Using lpf, recompute n as prime factorization in pf-form"""
  pf = []
  while n != 1:
    exponent = 1
    complement = n // lpf[n]
    while lpf[complement] == lpf[n]:
      exponent += 1
      complement //= lpf[n]
    pf.append((lpf[n], exponent))
    n = complement
  return pf

def generate_normal_factors(pf):
  """Given pf in pf-form, generator for all factors in normal form"""  
  for exponents in product(*[range(exponent+1) for _, exponent in pf]):
    yield reduce(
      lambda a,b : a*b,
      (prime ** exponent for (prime, _), exponent in zip(pf, exponents)),
      1
    )

###

N = int(sys.argv[1])
print(f"N = {N}")

MAX_LPF_LIMIT = 10000
lpf = get_lpf(MAX_LPF_LIMIT)

# all_cuboids = set()

def case_A(c):
  # print(f"c = {c}")
  if c % 4 != 0: return 0
  factors = list(generate_normal_factors(get_prime_factorization(lpf, c // 2)))
  res = 0
  for m in factors:
    for n in factors:
      if m <= n: continue
      if m % 2 == 1 and n % 2 == 1: continue
      if gcd(m, n) != 1: continue

      k = (c // 2) // (m * n)
      # print(f"  m = {m}, n = {n}, k = {k}")
      ab_sum = k * (m**2 - n**2)
      # print(f"  ab_sum = {ab_sum}")
      max_a = ab_sum // 2
      min_a = max(ab_sum - c, 1)
      # for a in range(min_a, max_a+1):
      #   b = ab_sum - a
      #   # assert sqrt((a+b)**2 + c**2)**2 == (a+b)**2 + c**2, f"{(a, b, c)}"
      #   all_cuboids.add((a, b, c))
      # print(f"  min_a = {min_a}, max_a = {max_a}, delta = {max(max_a - min_a + 1, 0)}")
      # ab_sum - a <= c
      # a must be greater than or equal to ab_sum - c
      res += max(max_a - min_a + 1, 0)
  return res

def case_B(c):
  # print(f"c = {c}")
  factors = list(generate_normal_factors(get_prime_factorization(lpf, c)))
  res = 0
  for m_plus_n in factors:
    for m_minus_n in factors:
      if m_plus_n % 2 == 0 or m_minus_n % 2 == 0: continue
      if gcd(m_plus_n, m_minus_n) != 1: continue
      m, n = (m_plus_n + m_minus_n) // 2, (m_plus_n - m_minus_n) // 2
      if m <= n: continue
      if m <= 0 or n <= 0: continue

      k = c // (m_plus_n * m_minus_n)
      # print(f"  m = {m}, n = {n}, k = {k}")

      ab_sum = 2*k*m*n
      # print(f"  ab_sum = {ab_sum}")
      max_a = ab_sum // 2
      min_a = max(ab_sum - c, 1)
      # for a in range(min_a, max_a+1):
      #   b = ab_sum - a
      #   all_cuboids.add((a, b, c))
        # assert sqrt((a+b)**2 + c**2)**2 == (a+b)**2 + c**2, f"{(a, b, c)}"


      # print(f"  min_a = {min_a}, max_a = {max_a}, delta = {max(max_a - min_a + 1, 0)}")
      res += max(max_a - min_a + 1, 0)
  return res

c = 0
total = 0
while total <= N:
  c += 1

  total += case_A(c)
  total += case_B(c)
  # print(f"total = {total} and c = {c}")
  # input()

print(f"total = {total} and M = {c}")
# for a, b, c in all_cuboids:
#   assert a <= b
#   assert b <= c
#   assert sqrt((a+b)**2 + c**2)**2 == (a+b)**2 + c**2, f"{(a, b, c)}"