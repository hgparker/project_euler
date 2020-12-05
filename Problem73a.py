# Method 1 
#  Repeatedly take the mediant between existing adjacent solutions until denominator is too big
# Time complexity O(S) where S is the answer

import sys


d = int(sys.argv[1])

stack = [[3, 2]]
num = 0

while stack:
  leftDenominator, rightDenominator = stack.pop()
  if leftDenominator + rightDenominator > d:
    continue
  num += 1
  stack.append([leftDenominator, leftDenominator + rightDenominator])
  stack.append([leftDenominator + rightDenominator, rightDenominator])

print(num)