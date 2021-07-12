import sys

sys.path.append("../EulerLibrary")

from numbertheory import allPrimes, isPrimeFast

primes = allPrimes(10000)

def concatenate(p, q):
  return int(str(p) + str(q))

breakout = False
for a in range(len(primes)):
  for b in range(a+1, len(primes)):
    if not isPrimeFast(concatenate(primes[a], primes[b])) or not isPrimeFast(concatenate(primes[b], primes[a])): continue
    for c in range(b+1, len(primes)):
      if not isPrimeFast(concatenate(primes[a], primes[c])) or not isPrimeFast(concatenate(primes[c], primes[a])): continue
      if not isPrimeFast(concatenate(primes[b], primes[c])) or not isPrimeFast(concatenate(primes[c], primes[b])): continue
      for d in range(c+1, len(primes)):
        if not isPrimeFast(concatenate(primes[a], primes[d])) or not isPrimeFast(concatenate(primes[d], primes[a])): continue
        if not isPrimeFast(concatenate(primes[b], primes[d])) or not isPrimeFast(concatenate(primes[d], primes[b])): continue
        if not isPrimeFast(concatenate(primes[c], primes[d])) or not isPrimeFast(concatenate(primes[d], primes[c])): continue
        for e in range(d+1, len(primes)):
          if not isPrimeFast(concatenate(primes[a], primes[e])) or not isPrimeFast(concatenate(primes[e], primes[a])): continue
          if not isPrimeFast(concatenate(primes[b], primes[e])) or not isPrimeFast(concatenate(primes[e], primes[b])): continue
          if not isPrimeFast(concatenate(primes[c], primes[e])) or not isPrimeFast(concatenate(primes[e], primes[c])): continue
          if not isPrimeFast(concatenate(primes[d], primes[e])) or not isPrimeFast(concatenate(primes[e], primes[d])): continue
          print(sum([primes[a], primes[b], primes[c],primes[d], primes[e]]))
          breakout = True
          if breakout: break
        if breakout: break
      if breakout: break
    if breakout: break
  if breakout: break