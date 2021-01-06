# Method 1 : use recurrence relation & check first x pairs

import sys

def numDigits(q):
  count = 1
  while q > 0:
    count += 1
    q //= 10
  return count

numPenult = 3
denPenult = 2
numUlt = 7
denUlt = 5
count = 0

for k in range(3, int(sys.argv[1])+1):
  # print([numUlt, denUlt, numDigits(numUlt), numDigits(denUlt)])
  numNew = 2*numUlt + numPenult
  denNew = 2*denUlt + denPenult

  if numDigits(numNew) != numDigits(denNew):
    count += 1

  numPenult, denPenult = numUlt, denUlt
  numUlt, denUlt = numNew, denNew


print(count)