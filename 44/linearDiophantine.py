
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

# print(getPositiveSolution(57, 121, 30302))
