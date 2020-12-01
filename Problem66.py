import math
import sys

# Method 1
# Get sequence of convergents and test each one

# get periodic continued fraction for sqrt(D) according to convention [a0, [a1...ar]]
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

# check to see if some pair satisfies Pell's equation
def checkPair(x, y, D):
  return (x ** 2) - D * (y ** 2) == 1

# find first convergent that works

def getSolutionConvergent(D):
  a, repetend = getPCF(D)
  p_penult = a
  q_penult = 1
  if checkPair(p_penult, q_penult, D):
    return p_penult  
  p_ult = a*repetend[0] + 1
  q_ult = repetend[0]
  if checkPair(p_ult, q_ult, D):
    return p_ult
  k = 1
  while True:
    p = repetend[k] * p_ult + p_penult
    q = repetend[k] * q_ult + q_penult
    if checkPair(p, q, D):
      return p
    p_penult, q_penult = p_ult, q_ult
    p_ult, q_ult = p, q 
    k = (k + 1) % len(repetend)

max_min_solution = 3
hardest_D = 2

for k in range(2, int(sys.argv[1])):
  s = math.sqrt(k)
  if math.floor(s) ** 2 == k:
    continue
  min_solution = getSolutionConvergent(k)
  if min_solution > max_min_solution:
    max_min_solution = min_solution
    hardest_D = k 

print(hardest_D)