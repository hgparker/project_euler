def get_best_numeral(n):
  res = ""

  num_M = n // 1000
  res += "M" * num_M
  n -= 1000 * num_M

  for scale, unit, fiver, tenner in [(100, "C", "D", "M"), (10, "X", "L", "C"), (1, "I", "V", "X")]:
    if n >= 9 * scale:
      res += unit + tenner      
      n -= 9 * scale
    elif n >= 8 *scale:
      res += fiver + (unit * 3)
      n -= 8 * scale
    elif n >= 7 *scale:
      res += fiver + (unit * 2)  
      n -= 7 * scale
    elif n >= 6 *scale:
      res += fiver + unit  
      n -= 6 * scale
    elif n >= 5 *scale:
      res += fiver
      n -= 5 * scale
    elif n >= 4 *scale:
      res += unit + fiver
      n -= 4 * scale
    elif n >= 3 *scale:
      res += unit * 3
      n -= 3 * scale
    elif n >= 2 *scale:
      res += unit * 2
      n -= 2 * scale
    elif n >= scale:
      res += unit
      n -= scale
  return res

def interpret(s):
  n = 0
  if s[:4] == "MMMM":
    n += 4000
    s = s[4:]
  elif s[:3] == "MMM":
    n += 3000
    s = s[3:]
  elif s[:2] == "MM":
    n += 2000
    s = s[2:]
  elif s[:1] == "M":
    n += 1000
    s = s[1:]

  for scale, unit, fiver, tenner in [(100, "C", "D", "M"), (10, "X", "L", "C"), (1, "I", "V", "X")]:
    if s[:9] == unit*9:
      n += 9 * scale
      s = s[9:]
    if s[:5] == fiver + unit*4:
      n += 9 * scale
      s = s[5:]
    if s[:2] == unit + tenner:
      n += 9 * scale
      s = s[2:]

    if s[:8] == unit*8:
      n += 8 * scale
      s = s[8:]
    if s[:4] == fiver + unit*3:
      n += 8 * scale
      s = s[4:]

    if s[:7] == unit*7:
      n += 7 * scale
      s = s[7:]
    if s[:3] == fiver + unit*2:
      n += 7 * scale
      s = s[3:]

    if s[:6] == unit*6:
      n += 6 * scale
      s = s[6:]
    if s[:2] == fiver + unit:
      n += 6 * scale
      s = s[2:]

    if s[:5] == unit*5:
      n += 5 * scale
      s = s[5:]
    if s[:1] == fiver:
      n += 5 * scale
      s = s[1:]
    
    if s[:4] == unit*4:
      n += 4 * scale
      s = s[4:]
    if s[:2] == unit + fiver:
      n += 4 * scale
      s = s[2:]

    if s[:3] == unit*3:
      n += 3 * scale
      s = s[3:]

    if s[:2] == unit*2:
      n += 2 * scale
      s = s[2:]

    if s[:1] == unit*1:
      n += 1 * scale
      s = s[1:]
  return n

N = 1000
ans = 0
while N > 0:
  s = input()
  delta = len(s) - len(get_best_numeral(interpret(s)))
  print(f"Received {s} of len {len(s)} -> {get_best_numeral(interpret(s))} with delta = {delta}")
  ans += delta
  N -= 1
print(N)
print(f"ans = {ans}")