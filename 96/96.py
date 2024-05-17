from math import inf

def iterate_through_affected(a, b):
  for col in range(9):
    if col != b:
      yield a, col
  for row in range(9):
    if row != a:
      yield row, b
  tl_row, tl_col = a // 3, b // 3
  for dr in range(3):
    for dc in range(3):
      if (3*tl_row + dr != a) and (3*tl_col + dc != b):
        yield 3*tl_row + dr, 3*tl_col + dc

# print(list(iterate_through_affected(3, 4)))

def get_current_possible(grid):
  current = [[0] * 9 for _ in range(9)]
  p = [[[True] * 10 for col in range(9)] for row in range(9)]
  for a in range(9):
    for b in range(9):
      p[a][b][0] = False
      if grid[a][b] != "0":
        current[a][b] = int(grid[a][b])
        for c, d in iterate_through_affected(a, b):
          p[c][d][current[a][b]] = False
        for d in range(1, 10):
          if d != current[a][b]:
            p[a][b][d] = False
  return current, p

def grand_dfs(c, p):

  def _dfs():
    ba, bb, val = 0, 0, inf
    for a in range(9):
      for b in range(9):
        if c[a][b] == 0:
          if sum(p[a][b]) < val:
            ba, bb, val = a, b, sum(p[a][b])
    
    # print(f"Going to try choosing for {(ba, bb)} with {val} possibilities")
    # if nothing unassigned
    if val == inf:
      return True
    
    # try possibilities for ba, bb
    possibles = [d for d in range(1, 10) if p[ba][bb][d]]
    for possible in possibles:
      c[ba][bb] = possible
      deltas = []
      for a, b in iterate_through_affected(ba, bb):
        if p[a][b][possible]:
          p[a][b][possible] = False
          deltas.append((a, b))    
      res = _dfs()
      if res: 
        return res
      for a, b in deltas:
        p[a][b][possible] = True
      c[ba][bb] = 0
    pass
  
  return _dfs()
  
# grid = [
#   "003020600",
#   "900305001",
#   "001806400",
#   "008102900",
#   "700000008",
#   "006708200",
#   "002609500",
#   "800203009",
#   "005010300",
# ]

N = 50
ans = 0
while N > 0:
  input()
  print(f"N = {N}")
  grid = []
  while len(grid) < 9:
    grid.append(input())
  c, p = get_current_possible(grid)
  grand_dfs(c, p)
  ans += 100*c[0][0] + 10*c[0][1] + c[0][2]
  N -= 1

print(f"ans = {ans}")
# c, p = get_current_possible(grid)
# grand_dfs(c, p)
# print(c)
# print()
# for row in c:
#   print(" ".join(str(ele) for ele in row))