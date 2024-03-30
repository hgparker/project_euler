import sys
from math import inf

LIMIT = int(sys.argv[1])

# print(f"{LIMIT = }")

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

def get_sigma(N):
  lpf = get_lpf(N)
  sigma = [1] * (N+1)
  for k in range(2, N+1):
    if lpf[k] == k:
      sigma[k] = k+1
    else:
      curr = k // lpf[k]
      e = 1
      while lpf[curr] == lpf[k]:
        curr //= lpf[k]
        e += 1
      sigma[k] = sigma[curr] * ((lpf[k]**(e+1) - 1) // (lpf[k]-1))
  return sigma

def get_proper_divisor_sums(N):
  return [sigma-k for k, sigma in enumerate(get_sigma(N))]

sieve = get_proper_divisor_sums(LIMIT)

print(f"divisor sums calculated")

epoch = [-1] * (LIMIT+1)

# found_cycle, node on cycle
def get_cycle_status(node):
  if epoch[node] != -1:
    return False, inf
  curr = node
  while curr > 1 and curr <= LIMIT and epoch[curr] == -1:
    epoch[curr] = node
    curr = sieve[curr]
  if curr <= 1 or curr > LIMIT or epoch[curr] != node:
    return False, None
  return True, curr

def get_cycle_period_minimum(node):
  # print(f"called with {node = }")
  cycle_length = 1
  minimum = node
  curr = sieve[node]
  while curr != node:
    curr = sieve[curr]
    minimum = min(minimum, curr)
    cycle_length += 1
  return cycle_length, minimum

max_cycle_length = 0
min_cycle_member = inf

for n in range(1, LIMIT+1):
  found_cycle, node = get_cycle_status(n)
  if found_cycle:
    cycle_length, min_node = get_cycle_period_minimum(node)
    if cycle_length > max_cycle_length:
      max_cycle_length = cycle_length
      min_cycle_member = min_node
    elif cycle_length == max_cycle_length and min_node < min_cycle_member:
      min_cycle_member = min_node

# print(f"{min_cycle_member = }")
