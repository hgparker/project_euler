from math import ceil, floor

def numdigits(n):
  return len(str(n))

least = 1
most = 9
n = 1
total = 0
while True:
  print("n, ",n)
  minRoot = ceil(pow(least, 1/n))
  maxRoot = floor(pow(most, 1/n))
  if numdigits(maxRoot ** n) > n:
    maxRoot -= 1
  if maxRoot < minRoot: break
  total += maxRoot-minRoot+1
  n += 1
  least *= 10
  most = least*10 - 1

print(total)