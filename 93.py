from itertools import combinations, combinations_with_replacement, permutations

def legalPostfix(expression):
  chars = {"a", "b", "c", "d"}
  numChars = 0
  for term in expression:
    if term in chars:
      numChars += 1
    else:
      if numChars < 2: return False
      numChars -= 1
  return True

def evalPostfix(expression, values):
  stack = []
  chars = {"a", "b", "c", "d"}
  for term in expression:
    if term in chars:
      stack.append(values[term])
    else:
      q = stack.pop()
      p = stack.pop()
      if term == "+":
        stack.append(p+q)
      elif term == "-":
        stack.append(p-q)
      elif term == "*":
        stack.append(p*q)
      else:
        if q == 0: return -1
        stack.append(p/q)
  return stack[-1]

postfixes = []

for ops in combinations_with_replacement("+-*/", 3):
  rawMaterial = ops + ("a", "b", "c", "d")
  for expression in permutations(rawMaterial):
    if legalPostfix(expression): postfixes.append(expression)

bestMaxReachable = 0
bestFour = (-1,-1,-1,-1)

for a, b, c, d in combinations([1,2,3,4,5,6,7,8,9], 4):
  reachable = set()
  values = {"a": a, "b": b, "c":c, "d": d}
  for postfix in postfixes:
    reachable.add(evalPostfix(postfix, values))
  maxReachable = 0
  while maxReachable+1 in reachable:
    maxReachable += 1
  if maxReachable > bestMaxReachable:
    bestMaxReachable = maxReachable
    bestFour = (a,b,c,d)

print(bestFour)