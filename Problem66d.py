import math
import sys

# Method 4
# On asymptotic assumption that only primes work out, only test primes by sieving

def getPCF(D):
  m = 0
  d = 1
  a = int(math.floor(math.sqrt(D)))
  output = [a, []]
  while a != 2 * output[0]:
    mn = d*a - m
    dn = (D - (mn*mn)) / d
    an = int((output[0] + mn) / dn)
    output[1].append(an)
    m, d, a = mn, dn, an
  return output

# calc and return first convergent that works

def getSolutionConvergent(D):
  a, repetend = getPCF(D)
  r = len(repetend) -1

  if r % 2 == 0:
    n = 2*r
  else:
    n = r - 1
  
  p_penult = a
  q_penult = 1

  p_ult = a*repetend[0] + 1
  q_ult = repetend[0]
  if n == 0:
    # print([D, 0, p_ult])
    return p_ult
  
  k = 1
  while True:
    p = repetend[k % len(repetend)] * p_ult + p_penult
    q = repetend[k % len(repetend)] * q_ult + q_penult
    if n == k:
      # print([D, n, p])
      return p
    p_penult, q_penult = p_ult, q_ult
    p_ult, q_ult = p, q 
    k += 1

max_min_solution = 3
hardest_D = 2
D = int(sys.argv[1])
sieve = [True] * (D+1) 
for k in range(2, D + 1):
  if not sieve[k]:
    continue
  min_solution = getSolutionConvergent(k)
  if min_solution > max_min_solution:
    max_min_solution = min_solution
    hardest_D = k
    # print(["new max = ", hardest_D])
  for p in range(2*k, D+1, k):
    sieve[p] = False

print(hardest_D)