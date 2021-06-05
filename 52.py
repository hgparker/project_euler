from itertools import combinations, permutations

def convert(perm):
  result = 0
  for k in range(len(perm)):
    result *= 10
    result += perm[k]
  return result

solutions = []

for numDigits in range(2, 11):
  if solutions:
    break
  for digits in combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numDigits):
    perms = sorted([convert(perm) for perm in permutations(digits) if perm[0] != 0])
    start = 0
    twoTimes = 0
    threeTimes = 0
    fourTimes = 0
    fiveTimes = 0
    sixTimes = 0

    while start < len(perms):
      while twoTimes < len(perms) and perms[twoTimes] < 2*perms[start]: twoTimes += 1
      while threeTimes < len(perms) and perms[threeTimes] < 3*perms[start]: threeTimes += 1
      while fourTimes < len(perms) and perms[fourTimes] < 4*perms[start]: fourTimes += 1
      while fiveTimes < len(perms) and perms[fiveTimes] < 5*perms[start]: fiveTimes += 1
      while sixTimes < len(perms) and perms[sixTimes] < 6*perms[start]: sixTimes += 1
      if sixTimes == len(perms): break
      if 2*perms[start] == perms[twoTimes] and 3*perms[start] == perms[threeTimes] and 4*perms[start] == perms[fourTimes] and 5*perms[start] == perms[fiveTimes] and 6*perms[start] == perms[sixTimes]:
        solutions.append(perms[start])
      start += 1
    
print(min(solutions))
