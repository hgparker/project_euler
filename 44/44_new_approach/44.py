from math import sqrt
import sys

def get_apts(c_bound):
  triplets = set()

  stack = [(1,1,1), (1, 2, 2)]

  while stack:
    a, b, c = stack.pop()
    if c > c_bound:
      continue

    if a != b:
      triplets.add((a, b, c) if a <= b else (b, a, c))

    stack.append((a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c))
    stack.append((a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c))
    stack.append((-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c))

  return triplets

def get_pentagonal(n):
  return n * (3*n - 1) // 2

def is_pentagonal(x):
  discriminant = sqrt(1+24*x)
  return discriminant*discriminant == 1+24*x and discriminant % 6 == 5

bound = int(sys.argv[1])
for a, b, c in get_apts(bound):
  if a % 6 != 5 or b % 6 != 5 or c % 6 != 5:
    continue
  a = (a+1) // 6
  b = (b+1) // 6
  difference = get_pentagonal(b) - get_pentagonal(a)
  if is_pentagonal(difference):
    print(f"EXAMINE THIS ONE: {b-a}")