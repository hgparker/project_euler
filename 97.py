# Fast modular exponentiation

mod = 10000000000

power = 7830457
multiplier = 2
product = 1

while power > 0:
  if power % 2 == 1: product = (product * multiplier) % mod
  multiplier = (multiplier * multiplier) % mod
  power //= 2

print((28433 * product + 1) % mod)