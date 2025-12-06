import sys
from math import inf

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

# numerical partition: {val: weight} : (product) val^weight = number
def get_numerical_partition_signature(numerical_partition):
  return tuple(sorted(numerical_partition.items()))

def unpack_numerical_partition_from_signature(numerical_partition_signature):
  return {val: weight for val, weight in numerical_partition_signature}

# numerical_multipartitions = {numerical_partition_signature}

def get_numerical_multipartitions(prev_numerical_multipartitions, prime):
  """
  (1) Given prev_numerical_multipartitions for n // prime and prime,
    return numerical_partitions, where
  (2) numerical_partitions is {numerical_partition_signature, ...}, and where
    numerical_partition_signature = ((val, weight), ...) with distinct val's in sorted order  
  """
  numerical_partitions = set()
  for prev_multipartition_signature in prev_numerical_multipartitions:
    prev_multipartition = unpack_numerical_partition_from_signature(prev_multipartition_signature)
    # add prime by itself
    numerical_partition = prev_multipartition.copy()
    if prime in numerical_partition:
      numerical_partition[prime] += 1
    else:
      numerical_partition[prime] = 1
    numerical_partitions.add(get_numerical_partition_signature(numerical_partition))
    for val, weight in prev_multipartition.items():
      numerical_partition = {}
      for other_val, other_weight in prev_multipartition.items():
        if other_val == val:
          if other_weight > 1:
            numerical_partition[val] = weight - 1
        else:
          numerical_partition[other_val] = other_weight

      new_val = val * prime
      if new_val in numerical_partition:
        numerical_partition[new_val] += 1
      else:
        numerical_partition[new_val] = 1
      numerical_partitions.add(get_numerical_partition_signature(numerical_partition))
  return numerical_partitions

###

MAX_K = int(sys.argv[1])
print(f"MAX_K = {MAX_K}")

MAX_N = 20000
lpf = get_lpf(MAX_N)
all_numerical_partitions = [None] * (MAX_N + 1)

mps = [inf] * (MAX_K+1)
num_solved = 0

break_all = False
for n in range(2, MAX_N+1):
  if lpf[n] == n:
    all_numerical_partitions[n] = {((n, 1),)}
  else:
    all_numerical_partitions[n] = get_numerical_multipartitions(all_numerical_partitions[n // lpf[n]], lpf[n])
  # print(f"n = {n}")
  # print(all_numerical_partitions[n])
  
  for numerical_partition_sig in all_numerical_partitions[n]:
    # print(f"np sig = {numerical_partition_sig}")  
    np = unpack_numerical_partition_from_signature(numerical_partition_sig)
    provided_sum = sum(val*weight for val, weight in np.items())
    num_entries = sum(np.values())
    if num_entries == 1: continue
    num_ones = n - provided_sum
    k = num_ones + num_entries
    # print(f"generates size of set {k}")
    # input()

    if k <= MAX_K and mps[k] == inf:
      num_solved += 1
      mps[k] = n
      if num_solved == MAX_K - 1:
        break_all = True
        break

  if break_all: break

if num_solved != MAX_K - 1:
  print(f"MAX_N was set too low!!!!")
else:
  ans = sum(set(mps[2:]))
  print(f"ans = {ans}")