# Method1
# solution must be of form ab/bd, use algebraic solutions for third variable in terms of a and b
# trying other way gets solutions > 1
# thus, only have to try around 50 possibilities

import itertools as it
import math

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numProduct = 1
denProduct = 1

for a, b in it.permutations(digits, 2):
  if 10*a*b % (9*a+b) == 0:
    d = 10*a*b // (9*a + b)
    numProduct *= a
    denProduct *= d

print(denProduct // math.gcd(numProduct, denProduct))