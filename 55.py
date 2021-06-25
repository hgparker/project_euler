from math import inf

def lychrelize(n):
  return n + int(str(n)[::-1])

def isPalindrome(n):
  return str(n) == str(n)[::-1]

memo = {}

def lychrelDistance(n, depth):
  if n in memo:
    return memo[n]
  if depth > 50:
    memo[n] = -inf
    return memo[n]
  if isPalindrome(n):
    memo[n] = 0
    return 0
  return 1+lychrelDistance(lychrelize(n), depth+1)

def isLychrelNumber(n):
  return (1+lychrelDistance(lychrelize(n), 1)) == -inf

numLychrel = 0
for k in range(1, 10000):
  if isLychrelNumber(k): numLychrel += 1
print(numLychrel)