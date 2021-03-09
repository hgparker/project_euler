# Method 4: 

import sys
from functools import reduce

numDigits = int(sys.argv[1])

facs = [1]
while len(facs) < max(10, numDigits+1):
  facs.append(facs[-1] * len(facs))

def digitize(n):
  digitCount = [0] * 10
  while n > 0:
    digit = n % 10
    digitCount[digit] += 1
    n //= 10
  return tuple(digitCount)

pairs = {}
finalPairs = {}
for k in range(1, 10):
  pairs[facs[k]] = pairs.get(facs[k], 0) + 1

k=1
while k < numDigits:
  newPairs = {}
  for key in pairs:
    m = digitize(key)
    finalPairs[m] = finalPairs.get(m, 0) + pairs[key]
    for n in range(10):
      newPairs[key+facs[n]] = newPairs.get(key+facs[n], 0) + pairs[key]
  pairs = newPairs
  k += 1

for key in pairs:
    m = digitize(key)
    finalPairs[m] = finalPairs.get(m, 0) + pairs[key]


# print(pairs)
# print(len(pairs))

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

def calculate(n):
  if n in memoizedTuples: return memoizedTuples[n]
  sum = 0
  for digit, number in enumerate(n):
    sum += facs[digit] * number
  if sum in nonRepeat: memoizedTuples[n] = nonRepeat[sum]+1
  else: memoizedTuples[n] = calculate(digitize(sum)) + 1
  return memoizedTuples[n]

print("Begin phase2")

count = 0
for m in finalPairs:
  if calculate(m) == 59:
    count += finalPairs[m]

print(count)
# print(calculate(digitize(367945)))