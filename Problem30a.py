# Method 1
# Generate out as many solutions as possible exploring from x to 10x+k
# Use digit format to make calculating successors easy O(1) => limited by upper bound of only six digits numbers => O(L) time where L is upper bound
# kill branches where 9m > f(m) - m + 9^5
# DFS

import sys

power = int(sys.argv[1])
powers = [k ** power for k in range(10)]

sum = 0
stack = [(k, powers[k]) for k in range(1, 10)] # (m, f(m))

while len(stack) > 0:
  m, fm = stack.pop()
  if m == fm:
    sum += m

  if 9*m <= fm - m + powers[9]:
    for k in range(10):
      stack.append((10*m + k, fm + powers[k]))

print(sum-1) # b/c 1 doesn't coun
