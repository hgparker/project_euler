# Try permutations + isPrime()
# All 8 or 9 digit pandigitals are divisible by three, so just look at 7.

def isPrime(n):
  if n < 2: return False
  if n == 2 or n == 3: return True
  if n % 2 == 0 or n % 3 == 0: return False
  k = 5
  while k*k <= n:
    if n % k == 0: return False
    if n % (k + 2) == 0: return False
    k += 6
  return True

from itertools import permutations

for combo in permutations([7,6,5,4,3,2,1]):
  n = 1000000* combo[0] + 100000*combo[1] + 10000 * combo[2] + 1000 * combo[3] + 100*combo[4] + 10*combo[5] + combo[6]
  if isPrime(n):
    print(n)
    break