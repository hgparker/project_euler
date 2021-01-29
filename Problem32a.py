# Method 1
# We exploit the fact that if m1 has a digits, m2 b digits, then a+b=5
  # and that w/o loss of generality m1 < m2
  # thus, try m1 w/ 1 digit, m2 w/ four
  # m1 / 2 digits, m2 with three
  # save hits in set
  # ~120,000 possibilities to check...much better than naive option of checking 20,000,000 ...

import itertools as it

digits = [n for n in range(1, 10)]

hash = set()

def acceptable(unavailable, product):
  alsoUnavailable = set()
  while product > 0:
    digit = product % 10
    if digit in unavailable or digit in alsoUnavailable or digit == 0:
      return False
    alsoUnavailable.add(digit)
    product //= 10
  return True

for fiveDigits in it.permutations(digits, 5):
  m1 = fiveDigits[0]
  m2 = fiveDigits[1] * 1000 + fiveDigits[2] * 100 + fiveDigits[3] * 10 + fiveDigits[4]
  
  fiveDigitsSet = set(fiveDigits)
  if acceptable(fiveDigitsSet, m1*m2):
    hash.add(m1*m2)  

  m1 = 10*m1 + fiveDigits[1]
  m2 %= 1000

  if acceptable(fiveDigitsSet, m1*m2):
    hash.add(m1*m2)  

print(sum(hash))