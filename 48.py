
import sys

N = int(sys.argv[1])

mod = 10 ** 10
sum = 0

for k in range(1, N+1):
  sum += pow(k, k, mod)
  sum %= mod

print(sum)