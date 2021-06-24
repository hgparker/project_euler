

def digitSum(n):
  return sum(map(int,list(str(n))))

greatest = 0
for a in range(1, 100):
  num = 1
  for b in range(1, 100):
    num *= a
    greatest = max(greatest, digitSum(num))

print(greatest)