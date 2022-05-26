
max_C = 300
triplets = set()

def generate(a,b,c):
  if c >= max_C: return

  triplets.add((a, b, c) if a <= b else (b, a, c))

  generate(a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c)
  # if a != b:
  generate(a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c)
  generate(-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c)

generate(1, 1, 1)
generate(1, 2, 2)

for a, b, c in sorted(triplets):
  print(a, b, c)