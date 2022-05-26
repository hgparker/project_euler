

def are_collinear(v1, v2):
  x1, y1 = v1
  x2, y2 = v2
  return x1 * y2 == x2 * y1

def are_orthogonal(v1, v2):
  x1, y1 = v1
  x2, y2 = v2
  return x1 * x2 + y1 * y2 == 0

N = 50

count = 0
for x1 in range(N+1):
  for y1 in range(N+1):
    if x1 == 0 and y1 == 0: continue
    for x2 in range(x1+1):
      for y2 in range(y1, N+1):
        if (x2 == 0 and y2 == 0) or (x2 == x1 and y2 == y1): continue
        if are_collinear((x1, y1), (x2, y2)): continue
        if are_orthogonal((x1, y1), (x2-x1, y2-y1)):
          count += 1

print(count*2 + N*N)