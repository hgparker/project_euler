import sys
sys.path.append("../EulerLibrary")

from numbertheory import negativePell

for x, y in negativePell(2, 1, 1):
  n = (x+1)//2
  m = (y+1)//2
  if n > 10 ** 12:
    print(m)
    break