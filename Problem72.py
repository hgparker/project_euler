# Method1...use Euler's totient function formula and sieve all the values <= 1 mil
# Runs in O(nlog(log(n))) just like regular sieve

import sys

d = int(sys.argv[1])
sieve = [k for k in range(d+1)]

sum = 0
for k in range(2, d+ 1):
  if sieve[k] == k:
    sieve[k] -= 1
    for t in range(2*k, d+1, k):
      sieve[t] = (sieve[t] * (k - 1)) // k
  sum += sieve[k]

print(sum)