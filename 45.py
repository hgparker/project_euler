from math import sqrt, floor

def isTriangular(q):
  d = sqrt(1+8*q)
  return floor(d) == d

def isPentagonal(q):
  d = sqrt(1+24*q)
  return floor(d) == d and d % 6 == 5 


n = 1
while True:
  h = n * (2*n-1)
  if isPentagonal(h) and isTriangular(h):
    print(h)
  n += 1