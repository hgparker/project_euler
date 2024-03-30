from itertools import combinations

dice = [combo for combo in combinations([0,1,2,3,4,5,6,7,8, 9], 6)]

num_workable = 0

def possible(d1, d2, a, b):
  if d1 in a and d2 in b:
    return True
  if d1 in b and d2 in a:
    return True
  return False

def work(a, b):
  return all(possible(d1, d2, a, b) for d1, d2 in [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (6, 4), (8, 1)])

def ready(a):
  return set(ele if ele != 9 else 6 for ele in a)

for a in range(len(dice)):
  for b in range(a, len(dice)):
    if work(ready(dice[a]), ready(dice[b])):
      num_workable += 1

print(f" num_workable = {num_workable}")
