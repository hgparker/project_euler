import sys

N = int(sys.argv[1])

sieve = [True] * N
primes = []

for k in range(2, N):
  if sieve[k]:
    primes.append(k)
    for p in range(2*k, N, k):
      sieve[p] = False

print("sieve finished")

primeSum = 5
bestPrimeSum = 5
primeIndex = 1
minWindowLength = 1
while primeSum < N:
  if sieve[primeSum]:
    bestPrimeSum = primeSum
    minWindowLength = primeIndex+1
  primeSum += primes[primeIndex+1] + primes[primeIndex+2]
  primeIndex += 2


windowLength = minWindowLength+1

while windowLength < N:
  primeSum = sum(primes[1:1+windowLength])
  if primeSum > N: break
  caboose = 1
  while primeSum < N:
    if sieve[primeSum]:
      bestPrimeSum = primeSum
    primeSum -= primes[caboose]
    caboose += 1
    primeSum += primes[caboose + windowLength-1]
  windowLength += 2
print(bestPrimeSum)