# Method 3: 
# Use recursion and memoization, as usual, but over a multiset of digits rather than numbers

import sys
# from itertools import combinations_with_replacement
from functools import reduce

numDigits = int(sys.argv[1])

def digitize(n):
  digitCount = [0] * 10
  while n > 0:
    digit = n % 10
    digitCount[digit] += 1
    n //= 10
  return tuple(digitCount)

nonRepeat = {}
nonRepeat[169]=3
nonRepeat[363601]=3
nonRepeat[1454]=3
nonRepeat[871]=2
nonRepeat[45361]=2
nonRepeat[45362]=2
nonRepeat[872]=2
nonRepeat[145]=1
nonRepeat[1]=1
nonRepeat[2]=1
nonRepeat[40585]=1

memoizedTuples = {}

facs = [1]
while len(facs) < max(10, numDigits+1):
  facs.append(facs[-1] * len(facs))

def calculate(n):
  if n in memoizedTuples: return memoizedTuples[n]
  sum = 0
  for digit, number in enumerate(n):
    sum += facs[digit] * number
  if sum in nonRepeat: memoizedTuples[n] = nonRepeat[sum]+1
  else: memoizedTuples[n] = calculate(digitize(sum)) + 1
  return memoizedTuples[n]

# def digitize2(numZeros, nonZeroDigits):
#   digitCount = [0] * 10
#   digitCount[0] = numZeros
#   for digit in nonZeroDigits:
#     digitCount[digit] += 1
#   return tuple(digitCount)

count = 0
sums = [0] * 10
for numZeros in range(numDigits):
  for numNonZeros in range(1, numDigits-numZeros+1):
    for numOnes in range(numNonZeros+1):
      sums[1] = numOnes
      for numTwos in range(numNonZeros+1-sums[1]):
        sums[2] = sums[1] + numTwos
        for numThrees in range(numNonZeros+1-sums[2]):
          sums[3] = sums[2] + numThrees
          for numFours in range(numNonZeros+1-sums[3]):
            sums[4] = sums[3] + numFours
            for numFives in range(numNonZeros+1-sums[4]):
              sums[5] = sums[4] + numFives
              for numSixes in range(numNonZeros+1-sums[5]):
                sums[6] = sums[5] + numSixes
                for numSevens in range(numNonZeros+1-sums[6]):
                  sums[7] = sums[6] + numSevens
                  for numEights in range(numNonZeros+1-sums[7]):
                    numNines = numNonZeros-sums[7]-numEights
                    m = (numZeros, numOnes, numTwos, numThrees, numFours, numFives, numSixes, numSevens, numEights, numNines)
                    if calculate(m) == 60:
                      divider = reduce(lambda a, b: a*b, map(lambda x: facs[x], m))
                      count += numNonZeros * facs[numNonZeros + numZeros - 1] // divider

# for numZeros in range(numDigits):
#   for numNonZeros in range(1, numDigits-numZeros+1):
#     for nonZeroDigits in combinations_with_replacement([1,2,3,4,5,6,7,8,9], numNonZeros):
#       m = digitize2(numZeros, nonZeroDigits)
#       if calculate(m) == 60:
#         divider = reduce(lambda a, b: a*b, map(lambda x: facs[x], m))
#         count += numNonZeros * facs[numNonZeros + numZeros - 1] // divider

print(count)