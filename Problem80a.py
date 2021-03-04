# Method1 : use Babylonian method

from decimal import *
from math import sqrt, floor
from functools import reduce

getcontext().prec = 1000010

def sumPlaces(num):
  root = Decimal(1)
  k = 15 # could do actual epsilon calculation here instead
  while k > 0:
    root = (root + num/root) / Decimal(2)
    k -= 1
  rootParts = str(root).split(".")
  return int(rootParts[0]) + reduce(lambda a, b: a+b, map(lambda q: int(q), rootParts[1][0:999999]))

sum = 0
for k in range(2, 100):
  if floor(sqrt(k)) ** 2 == k:
    continue
  sum += sumPlaces(k)
print(sum)
