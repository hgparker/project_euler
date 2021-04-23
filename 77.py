import sys

N = int(sys.argv[1])

sieve = [True] * N
primes = []

for k in range(2, N):
  if sieve[k]:
    primes.append(k)
    for p in range(2*k, N, k):
      sieve[p] = False

numPrimeSums = [0] * N
numPrimeSums[0] = 1

found = False
for prime in primes:
  for k in range(prime, N):
    numPrimeSums[k] += numPrimeSums[k-prime]

for k in range(len(numPrimeSums)):
  if numPrimeSums[k] > 5000:
    print(k)
    break

print(numPrimeSums)