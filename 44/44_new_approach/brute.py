from math import sqrt

max_C = 300

for a in range(1, max_C):
  for b in range(a, max_C):
    if a ** 2 + b ** 2 - 1 >= max_C **2:
      break
    real_c = sqrt(a ** 2 + b ** 2 - 1)
    if int(real_c) == real_c:
      print(a, b, int(real_c))

