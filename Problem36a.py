# Method 1
# Generate all decimal palindromes methodically
# Test odd ones for binary palindromicity
# The number of decimal palindromes with d digits is about 10^(d/2)
#  For all < 1m, then we only have to check ~2000 possibilities

import sys

def isBinaryPalindrome(original):
  working = original
  flipped = 0
  while working > 0:
    flipped <<= 1
    flipped += working % 2
    working >>= 1
  return original == flipped

digitLimit = int(sys.argv[1])

palindromeStack = [(0, 0)] + [(k, 1) for k in range(10)] # (pal, digits)
palSum = 0

while len(palindromeStack) > 0:
  pal, digits = palindromeStack.pop()
  if pal % 2 == 1 and isBinaryPalindrome(pal):
    palSum += pal
  if digits + 2 < digitLimit:
    palindromeStack.extend([(k * (10 ** (digits+1)) + pal*10 + k,digits+2) for k in range(10)])

print(palSum)