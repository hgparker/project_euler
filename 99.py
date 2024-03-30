from math import log

a = []

for t in range(1000):
  base, exp = [int(c) for c in input().split(",")]
  a.append((exp*log(base), t+1))

a.sort()
print(a[-3:])