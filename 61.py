from itertools import chain
from collections import defaultdict

def isFourDigits(n):
  return n >= 1000 and n < 10000

triangles = set()
squares = set()
pents = set()
hexes = set()
hepts = set()
octs = set()

for k in range(1, 200):
  t = (k * (k+1)) // 2
  if isFourDigits(t):
    triangles.add(t)

  t = k * k
  if isFourDigits(t):
    squares.add(t)

  t = (k * (3*k-1)) // 2
  if isFourDigits(t):
    pents.add(t)

  t = (k * (2*k-1))
  if isFourDigits(t):
    hexes.add(t)

  t = (k * (5*k-3)) // 2
  if isFourDigits(t):
    hepts.add(t)

  t = (k * (3*k-2))
  if isFourDigits(t):
    octs.add(t)


figurate = set()
for k in chain(triangles, squares, pents, hexes, hepts, octs):
  figurate.add(k)

def getFirstTwo(n):
  return str(n)[:2]

def getLastTwo(n):
  return str(n)[2:]

byFirstTwo = defaultdict(list)
for k in figurate:
  byFirstTwo[getFirstTwo(k)].append(k)

successors = {}
for k in figurate:
  successors[k] = byFirstTwo[getLastTwo(k)][:]

candidates = []

for oct in octs:
  for n1 in successors[oct]:
    for n2 in successors[n1]:
      for n3 in successors[n2]:
        for n4 in successors[n3]:
          for n5 in successors[n4]:
            if oct in successors[n5]:
              candidates.append((oct, n1, n2, n3, n4, n5))

for candidate in candidates:
  
  tri, sq, pent, hex, hept, oct = 0, 0, 0, 0, 0, 0
  
  for k in candidate:
    if k in triangles and k not in hexes: tri += 1
    if k in squares: sq += 1
    if k in pents: pent += 1
    if k in hexes: hex += 1
    if k in hepts: hept += 1
    if k in octs: oct += 1
  
  
  if tri == 1 and sq == 1 and pent == 1 and hex == 1 and hept == 1 and oct == 1:
    print(f"candidate: {candidate}, counts: {(tri, sq, pent, hex, hept, oct)}, sum: {sum(candidate)}")

