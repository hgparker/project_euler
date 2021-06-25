import sys
sys.path.append("../EulerLibrary")

from numbertheory import negPentagonal, posPentagonal

memo = {}
def partitions(n):
  if n in memo: return memo[n]
  if n == 0: return 1

  sign = 1
  ret = 0
  for k in posPentagonal():
    if k > n: break
    ret += sign*partitions(n-k)
    sign *= -1

  sign = 1
  for k in negPentagonal():
    if k > n: break
    ret += sign*partitions(n-k)
    sign *= -1

  memo[n] = ret % 1000000
  return ret

num = 1
while partitions(num) % 1000000 != 0:
  # print(num, partitions(num))
  num += 1
print(num)