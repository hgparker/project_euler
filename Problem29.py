import sys
import math

L = int(sys.argv[1])

# figure out how many novel values of a^b there are if a = x^p for minimum x
# store result in powerSum[p]
# figuring this out is O(L * log^2(L))
# we will next calculate what is a power of what and sum acording to value in powerSum
# this latter part is linear on L
# can comfortably solve L=5 million in < 1 minute, far advanced from the L=100 of the problem

maxPower = math.floor(math.log2(L))
powerSum = {1: L-1}

for power in range(2, maxPower+1):
  
  grid = [True] * (L + 1)
  numEliminated = 0

  for m in range(1, power):
    gcd = math.gcd(power, m)
    powerAdjusted = power // gcd
    mAdjusted = m // gcd

    start = 2 if mAdjusted == 1 else mAdjusted
    finish = L * mAdjusted // powerAdjusted

    for c in range(start, finish+1, mAdjusted):
      if grid[c] == True:
        numEliminated += 1
      grid[c] = False

  # print([power, L - 1 - numEliminated])
  powerSum[power] = L - 1 - numEliminated

print(powerSum)  

# figure out what is a power of what and sum that component

numDistinctPowers = 0
isPower = {}
numAlreadyCounted = 0
k = 2
while k*k <= L:
  if k in isPower:
    k += 1
    continue
  kNth = k * k
  n = 2
  while kNth <= L:
    isPower[kNth] = True
    numDistinctPowers += powerSum[n]
    numAlreadyCounted += 1
    kNth *= k
    n += 1
  k += 1

# contribute sum of non-Powers

numDistinctPowers += (L - 1 - numAlreadyCounted) * powerSum[1]

print(numDistinctPowers)




