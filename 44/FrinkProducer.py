
def getQuadraticResidue(m):
  for r in range(m):
    if (r ** 2) % m == m-1:
      return (r, m-r)

# Gets Bezout coefficients for a and b : ax + by = gcd(a,b)
def bezout(a, b): 
  x, y = 0, 1
  u, v = 1, 0
  while a:
    q =  b // a
    r = b % a

    m = x - u*q
    n = y - v*q   

    b = a
    a = r
    x = u
    y = v
    u = m
    v = n

  return (b, x, y) # (gcd, x, y) : gcd = a*x + b*y

def getInitial(a, b, right): # gets initial solution to ax + by = right
  gcd, x, y = bezout(a, b)
  if right % gcd: print("ERROR NO SOLUTION")
  x *= right // gcd
  y *= right // gcd
  return (gcd, x, y)

def getPositiveSolution(a, b, right):
  gcd, x, y = getInitial(a, b, right)
  if x > 0 and y > 0: return (x, y, a*x + b*y == right)
  dX, dY = b // gcd, a // gcd
  # print("initial:", x, y, a*x + b*y == right)
  if x < 0:
    m = (-x) // dX + 1
    x += m*dX
    y -= m*dY
    if y < 0: print("sorry no positive solution possible")
  else:
    m = (-y) // dY + 1
    x -= m*dX
    y += m*dY 
    if x < 0: print("sorry no positive solution possible")
  # print(x, y, a*x + b*y == right)    
  return (x, y)

# # # # # # #

# (a,b,c) = Pythagorean triplet
def frinkGenerator(a, b, c):
  r1, r2 = getQuadraticResidue(c)
  if r2 < r1: r1, r2 = r2, r1

  p1, q1 = getPositiveSolution(a, b, c*r1)
  p2, q2 = a-p1, b-q1
  t = 0
  while True:
    yield (a*t + p1, b*t + q1, c*t + r1)
    yield (a*t + p2, b*t + q2, c*t + r2)    
    t += 1

def pentagonal(p):
  return p * (3*p - 1) // 2

a, b, c = 65, 72, 97
for x, y, z in frinkGenerator(a,b,c):
  print(x % 6, y % 6, z % 6)
  if x % 2 == 0 or y % 2 == 0 or z % 2 == 0: continue
  tX, tY, tZ = x //2, y // 2, z // 2
  if tX % 3 != 2 or tY % 3 != 2 or tZ % 3 != 2: continue
  pX, pY, pZ = (tX+1)//3, (tY+1)//3, (tZ+1)//3
  print(pX, pY, pZ, pentagonal(pX) + pentagonal(pY) == pentagonal(pZ))
  # print(x, y, z, x ** 2 + y ** 2 == z ** 2 + 1)
