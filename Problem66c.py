import math
import sys

# Method 3
# Get Pell solution directly from sequence of convergents 
# Exploit patterns to rule out stuff
# (1) ignore odd r

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

# find first convergent that works

def getSolutionConvergent(D):
  a, repetend = getPCF(D)
  r = len(repetend) -1

  if r % 2 == 0:
    n = 2*r
  else: # ignore odd r
    return 0
  
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

for k in range(2, int(sys.argv[1]) + 1):
  s = math.sqrt(k)
  if math.floor(s) ** 2 == k:
    continue
  min_solution = getSolutionConvergent(k)
  if min_solution > max_min_solution:
    max_min_solution = min_solution
    hardest_D = k
    # print(["new max = ", hardest_D]) 

print(hardest_D)