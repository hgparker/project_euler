from math import sqrt, floor, inf

N = 2000000

def numRects(m, n):
  return (m * (m+1) * n * (n+1)) // 4

best = inf
area = -inf
m = 1

while True:
  lowN = floor(sqrt(8000000 / m / (m+1)))
  if lowN < m:
    break
  result = abs(N- numRects(m, lowN))
  if result < best:
    best = result
    area = m*lowN
  result = abs(N - numRects(m, lowN+1))
  if result < best:
    best = result
    area = m*(lowN+1)
  m += 1

print(best)