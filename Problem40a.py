# Method1
# Just grind it out :)
# Figure out how many digits we're dealing with
# Then calculate that digit
# O(logN)

def d(n):
  numDigits = 1
  n -= 1
  while n >= ((10 ** numDigits) - (10 ** (numDigits-1))) * numDigits:
    n -= ((10 ** numDigits) - (10 ** (numDigits-1))) * numDigits
    numDigits += 1
  num = (n // numDigits) + (10 ** (numDigits-1))
  digit = numDigits - 1 - (n % numDigits)
  while digit != 0:
    num //= 10
    digit -= 1
  return num % 10

print(d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000))

# print(d(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))



