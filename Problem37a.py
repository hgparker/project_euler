# Method 1
# Separately generate lists of left-truncatables and right-truncatables for each digit length
# Store in separate heaps ordered by digit length
# If one heap taps out, cut off the other heap accordingly
# left truncs: if p prime and in heap, check out [3|7|9]1*(p) as well as [2|5]1*(p) though after 
# checking the latter, don't feed them back into heap; start w/ [3,7]
# right truncs: if p prime and in heap, check out (p)1*[3|7|9] ; start w/ [2,3,5,7]

import heapq
import math

def isPrime(n):
  if n < 2: return False
  if n % 2 == 0 or n % 3 == 0:
    return False
  cF = 5
  while cF * cF <= n:
    if n % cF == 0 or n % (cF + 2) == 0:
      return False
    cF += 6
  return True

ltPrimes = set()
leftTruncs = [(1, 3), (1, 7)] # convention (number of digits, prime)
heapq.heapify(leftTruncs)

rtPrimes = set()
rightTruncs = [(1, 2), (1, 3), (1, 5), (1, 7)]
heapq.heapify(rightTruncs)

def ltAdvance():
  d, lt = heapq.heappop(leftTruncs)
  for digit in [3, 7, 9]:
    digitAdd = digit * (10 ** d)
    candidate = digitAdd + lt
    if isPrime(candidate):
      ltPrimes.add(candidate)
      heapq.heappush(leftTruncs,(d+1, candidate))
    numOnes = 1
    onesAdd = 10 ** d
    onesBooster = 10 ** d
    digitAdd *= 10
    candidate = digitAdd + onesAdd + lt
    while isPrime(candidate - digitAdd):
      if isPrime(candidate):
        ltPrimes.add(candidate)
        heapq.heappush(leftTruncs, (d + 1 + numOnes, candidate))
      numOnes += 1
      onesAdd = onesAdd*10 + onesBooster
      digitAdd *= 10
      candidate = digitAdd + onesAdd + lt
      
  for digit in [2,5]:
    digitAdd = digit * (10 ** d)
    candidate = digitAdd + lt
    if isPrime(candidate):
      ltPrimes.add(candidate)
      heapq.heappush(leftTruncs, (d+1, candidate))

    numOnes = 1
    onesAdd = 10 ** d
    onesBooster = 10 ** d
    digitAdd *= 10
    candidate = digitAdd + onesAdd + lt
    while isPrime(candidate - digitAdd):
      if isPrime(candidate):
        ltPrimes.add(candidate)
      numOnes += 1
      onesAdd = onesAdd*10 + onesBooster
      digitAdd *= 10
      candidate = digitAdd + onesAdd + lt
  return d

def rtAdvance():
  d, rt = heapq.heappop(rightTruncs)
  for digit in [3, 7, 9]:
    rtAdd = rt * 10
    candidate = rtAdd + digit
    if isPrime(candidate):
      rtPrimes.add(candidate)
      heapq.heappush(rightTruncs, (d+1, candidate))

    numOnes = 1
    onesAdd = 10
    rtAdd *= 10
    candidate = rtAdd + onesAdd + digit
    while isPrime(candidate // 10):
      if isPrime(candidate):
        rtPrimes.add(candidate)
        heapq.heappush(rightTruncs, (d + 1 + numOnes, candidate))
      numOnes += 1
      onesAdd = onesAdd*10 + 10
      rtAdd *= 10
      candidate = rtAdd + onesAdd + digit
  return d

maxlDigits = math.inf
maxrDigits = math.inf

while len(leftTruncs) > 0 or len(rightTruncs) > 0:
  if len(rightTruncs) == 0:
    if leftTruncs[0][0] > maxrDigits:
      break
    ltAdvance()
  elif len(leftTruncs) == 0:
    if rightTruncs[0][0] > maxlDigits:
      break
    rtAdvance()
  elif leftTruncs[0][0] < rightTruncs[0][0]:
    maxlDigits = ltAdvance()
  else:
    maxrDigits = rtAdvance()

print(sum(rtPrimes.intersection(ltPrimes)))