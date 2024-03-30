import sys
from math import sqrt, floor, inf
from bisect import bisect_right

LIMIT = int(sys.argv[1])

print(f"LIMIT = {LIMIT}")

### BEGIN LIBRARY CODE

def get_primes_lpf(N):
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

def get_primes(N):
  return get_primes_lpf(N)[0]

def right_le_ind(a, x):
  """
  (1) Returns INDEX of rightmost element less than or equal to x,
  (2) or -inf if no usch element exists
  """
  # print(f"    called with {(a, x)}")
  index = bisect_right(a, x)
  if index:
    return index-1
  return -inf

### END LIBRARY CODE

sqrt_limit = floor(sqrt(LIMIT))

print(f"sqrt_limit = {sqrt_limit}")

primes = get_primes(sqrt_limit)
p_squares = [prime*prime for prime in primes]
p_cubes = [prime*prime*prime for prime in primes if prime*prime*prime <= LIMIT]
p_fourths = [prime ** 4 for prime in primes if prime ** 4 <= LIMIT]

# print(f"{p_squares=}")
# print(f"{p_cubes=}")
# print(f"{p_fourths=}")


used = set()

for p_cube in p_cubes:
  # print(f"p_cube = {p_cube}")
  for p_fourth in p_fourths:
    # print(f"  p_fourth = {p_fourth}")
    if p_cube + p_fourth > LIMIT:
      # print(f"  hit breaking point from cube and fourth alone")
      break
    for p_square in p_squares:
      if p_cube + p_fourth + p_square > LIMIT:
        break
      used.add(p_cube + p_fourth + p_square)

    # print(f"  LIMIT - p_cube - p_fourth = {LIMIT - p_cube - p_fourth}")
    # index = right_le_ind(p_squares, LIMIT - p_cube - p_fourth)
    # print(f"  index = {index}")
    # if index == -inf:
    #   # print(f"  index is -inf, breaking")
    #   break
    # total_nums += index+1

print(f"Total_nums = {len(used)}")