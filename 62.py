from collections import defaultdict

def digitize(n):
  digits = [0] * 10
  while n > 0:
    digits[n % 10] += 1
    n //= 10
  return tuple(digits)

k = 1
hits = defaultdict(int)
first = {}
fives = set()
mostCubeDigits = 10

while True:
  if k ** 3 >= mostCubeDigits:
    mostCubeDigits *= 10
    if len(fives) > 0:
      print(min(fives) ** 3)
      break

  digits = digitize(k ** 3)

  if digits not in first:
    first[digits] = k
  
  hits[digits] += 1
  if hits[digits] == 5:
    fives.add(first[digits])
  if hits[digits] == 6:
    fives.remove(first[digits])  
  
  k += 1