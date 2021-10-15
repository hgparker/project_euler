from collections import defaultdict
from itertools import combinations
from math import inf

def allPrimes(n):
  sieve = [True] * n
  primes = []
  for k in range(2, n):
    if sieve[k]:
      primes.append(k)
      for p in range(2*k, n, k):
        sieve[p] = False
  return primes

def num_digits(n):
  return len(str(n))

N = 1000000
primes = allPrimes(N)
prime_set = set(primes)

primes_with_digit_length = defaultdict(set)
for prime in primes:
  primes_with_digit_length[num_digits(prime)].add(prime)

def renumber(digits_replaced, replacement_digit, original_number):
  replacement_digit = str(replacement_digit)
  number_str = list(str(original_number))
  for digit_replaced in digits_replaced:
    number_str[digit_replaced] = replacement_digit
  return int("".join(number_str))

visited = set() # (prime_number, digits_replaced)
families = set()

def family_explore(prime, digits_replaced):
  if (prime, digits_replaced) in visited: return
  family_size = 0
  smallest_prime_in_family = inf
  for replacement_digit in range(10):
    if digits_replaced[0] == 0 and replacement_digit == 0: continue
    renumbered = renumber(digits_replaced, replacement_digit, prime)
    if renumbered not in prime_set: continue
    smallest_prime_in_family = min(smallest_prime_in_family, renumbered)
    family_size += 1
    visited.add((renumbered, digits_replaced))
  if family_size == 8:
    families.add(smallest_prime_in_family)

for prime in primes:
  number_prime_digits = num_digits(prime)
  for number_of_digits_to_change in range(1, number_prime_digits):
    for digits_replaced in combinations([k for k in range(number_prime_digits)], number_of_digits_to_change):
      family_explore(prime, digits_replaced)
  if families: break

print(families, min(families))
