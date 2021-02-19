# Method 1: DFS w/ memoization

import sys

limit = int(sys.argv[1])

nC = [-1] * limit
nC[89] = 89
nC[1] = 1
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def calculate(n):
  if nC[n] != -1: return nC[n]
  sum = 0
  q = n
  while q > 0:
    sum += squares[q % 10]
    q //= 10
  nC[n] = calculate(sum)
  return nC[n]

count = 0
for k in range(1, limit):
  calculate(k)
  if nC[k] == 89: count += 1

print(count)