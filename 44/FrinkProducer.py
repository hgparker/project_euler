from math import sqrt

def is_pentagonal(q):
  candidate_square = 1+24*q
  candidate_square_root = int(sqrt(candidate_square))
  if candidate_square_root * candidate_square_root != candidate_square:
    return False
  if candidate_square_root % 6 != 5: return False
  return True


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


# (20, 99, 101)	(60, 91, 109)	(15, 112, 113)	(44, 117, 125)
# (88, 105, 137)	(17, 144, 145)	(24, 143, 145)	(51, 140, 149)
# (85, 132, 157)	(119, 120, 169)	(52, 165, 173)	(19, 180, 181)
# (57, 176, 185)	(104, 153, 185)	(95, 168, 193)	(28, 195, 197)
# (84, 187, 205)	(133, 156, 205)	(21, 220, 221)	(140, 171, 221)
# (60, 221, 229)	(105, 208, 233)	(120, 209, 241)	(32, 255, 257)
# (23, 264, 265)	(96, 247, 265)	(69, 260, 269)	(115, 252, 277)
# (160, 231, 281)	(161, 240, 289)	(68, 285, 293)
# a,b,c = (5, 12, 13)
# t = 0
# for x, y, z in frinkGenerator(a,b,c):

  # if (not x % 6 == 5) or (not y % 6 == 5) or (not z % 6 == 5): continue
  # print(x, y, z)
  # t += 1
  # if t > 100: break
  # p_x, p_y, p_z = (pentagonal((q+1)//6) for q in (x, y, z))  
  # print(p_x + p_y == p_z)
  # if is_pentagonal(p_y - p_x):
  #   print("WE GOT ONE!")
  #   print(p_y-p_x, p_x, p_y, p_x + p_y)
  #   break
  # print("\n")

  # print(x % 6, y % 6, z % 6)
  # if x % 2 == 0 or y % 2 == 0 or z % 2 == 0: continue
  # tX, tY, tZ = x //2, y // 2, z // 2
  # if tX % 3 != 2 or tY % 3 != 2 or tZ % 3 != 2: continue
  # pX, pY, pZ = (tX+1)//3, (tY+1)//3, (tZ+1)//3
  # print(pX, pY, pZ, pentagonal(pX) + pentagonal(pY) == pentagonal(pZ))
  # # print(x, y, z, x ** 2 + y ** 2 == z ** 2 + 1)

def get_first_few(triplet):
  a, b, c = triplet
  t = 0
  for x, y, z in frinkGenerator(a, b, c):
    yield x, y, z
    t += 1
    if t > 1000: return

triplets = [(3,4,5), (5,12,13), (8, 15, 17), (7,24,25), (20,21,29), (12, 35, 37),(9,40,41), (28, 45, 53)]

sets = [set(get_first_few(triplet)) for triplet in triplets]

for k in range(len(sets)-1):
  print(triplets[k], sets[-1].intersection(sets[k]))