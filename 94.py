from itertools import cycle

### LIBRARY CODE

def floor_square_root(n):
  """
  (1) Uses binary search to determine greatest number whose square is <= n
  (2) n must be positive integer (not 0) -- otherwise, add zero check
  """
  def attempt(r):
    return r*r <= n

  lo, hi = 1, n+1

  while lo + 1 < hi:
    mid = (lo + hi) // 2
    if attempt(mid):
      lo = mid
    else:
      hi = mid
  return lo

def sqrt_pcf_generator(D):
  """Given D, generate periodic continued fraction for sqrt(D) value by value"""
  m = 0
  d = 1
  a0 = floor_square_root(D)
  yield a0
  a = a0
  repetend = []
  while a != 2 * a0:
    mn = d*a - m
    dn = (D - (mn*mn)) // d
    an = (a0 + mn) // dn
    yield an
    repetend.append(an)
    m, d, a = mn, dn, an
  for a in cycle(repetend):
    yield a

def sqrt_convergents_generator(D):
  """Given D, generate progressively closer convergents for sqrt(D)"""
  h_prev, h_prev_prev = 1, 0
  k_prev, k_prev_prev = 0, 1
  for a in sqrt_pcf_generator(D):
    h = a*h_prev + h_prev_prev
    k = a*k_prev + k_prev_prev
    yield h, k
    h_prev, h_prev_prev = h, h_prev
    k_prev, k_prev_prev = k, k_prev

def pell_fundamental(D):
  """Given D, return fundamental solution to x^2 - D*y^2 = 1"""
  for h, k in sqrt_convergents_generator(D):
    if h ** 2 - D*(k**2) == 1:
      return h, k

def pell_generator(D):
  """Given fundamental solution (x1, y1) to x^2 - D*y^2 = 1, generate all others"""
  x_fund, y_fund = pell_fundamental(D)
  xk, yk = x_fund, y_fund
  while True:
    yield (xk, yk)
    xk_next = x_fund*xk + D*y_fund*yk
    yk_next = x_fund*yk + y_fund*xk
    xk, yk = xk_next, yk_next

def general_pell_generator(D, x1, y1):
  """
  (1) Given fundamental solution (x1, y1) to x^2 - D*y^2 = N,
      and corresponding to Pell's resolvent (x, y) to x^2 - D*y^2 = 1
  (2) Generate the dynasty of solutions to the generalized equation.
  (3) Keep in mind there will be as many dynasties as fundamental solutions 
  """
  yield x1, y1
  for x, y in pell_generator(D):
    yield x*x1 + D*y*y1, x*y1 + y*x1 

### END LIBRARY CODE

# LIMIT = 100
LIMIT = 1000000000
peri_sum = 0
print(f"Using {LIMIT = }")
for z, y in pell_generator(3):
  # print(f"{z = } {y = } {z**2 - 3*y**2 == 1}")
  if (z % 3) != 1:
    continue
  t = (z - 1) // 3
  # print(f"  {t = }")

  x = 2*t + 1
  # print(f"  {x = }")
  
  cand_peri = 3*x + 1
  # print(f"  {cand_peri = } {cand_peri <= LIMIT}")

  if cand_peri > LIMIT:
    break

  peri_sum += cand_peri
  # input()

for z, y in pell_generator(3):
  # print(f"{z = } {y = } {z**2 - 3*y**2 == 4}")
  if z % 3 != 2:
    continue
  
  t = (z + 1) // 3
  # print(f"  {t = }")
  
  x = 2*t - 1
  # print(f"  {x = }")

  cand_peri = 3*x - 1
  # print(f"  {cand_peri = } {cand_peri <= LIMIT}")

  if cand_peri > LIMIT:
    break

  peri_sum += cand_peri
  # input()

# to account for non-solution (1, 1,0)
peri_sum -= 2

print(f"{peri_sum = }")
