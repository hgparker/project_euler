

digitsAvailable = {0, 1,2,3,4,5,6,7,8,9}
d5possibles = [[0,3,6,9], [2,5,8], [1,4,7]]
d7possibles = [[0,7], [6], [5], [4], [3], [2, 9], [1,8]]
d8possibles = [0, None, 9, 8, 7, 6, 5, 4, 3, 2, 1]
d9possibles = [0, None, None, None, 9, 8, 7, 6, 5, 4, 3, 2, 1]
d10possibles = [0, None, None, None, None, None, None, None, 9, 8, 7, 6, 5, 4, 3, 2, 1]
ssSum = 0
for d3 in range(10):
  digitsAvailable.remove(d3)
  for d4 in [0,2,4,6,8]:
    if d4 not in digitsAvailable: continue
    digitsAvailable.remove(d4)
    for d6 in [0, 5]:
      if d6 not in digitsAvailable: continue
      digitsAvailable.remove(d6)
      s1 = (d3 + d4) % 3  
      for d5 in d5possibles[s1]:
        if d5 not in digitsAvailable: continue
        digitsAvailable.remove(d5)
        s2 = (100*d5 + 10*d6) % 7
        for d7 in d7possibles[s2]:
          if d7 not in digitsAvailable: continue
          digitsAvailable.remove(d7)
          s3 = (100*d6 + 10*d7) % 11
          d8 = d8possibles[s3]
          if d8 != None and d8 in digitsAvailable:
            digitsAvailable.remove(d8)
            s4 = (100*d7 + 10*d8) % 13
            d9 = d9possibles[s4]
            if d9 != None and d9 in digitsAvailable:
              digitsAvailable.remove(d9)
              s5 = (100*d8 + 10*d9) % 17
              d10 = d10possibles[s5]
              if d10 != None and d10 in digitsAvailable:
                digitsAvailable.remove(d10)
                base = 10000000* d3 + 1000000 * d4 + 100000*d5 + 10000*d6 + 1000*d7 + 100*d8 + 10*d9+ d10
                if 0 not in digitsAvailable:
                  ssSum += 2*base + sum(digitsAvailable) * 1100000000
                else:
                  ssSum += base + sum(digitsAvailable) * 1000000000
                digitsAvailable.add(d10)
              digitsAvailable.add(d9)
            digitsAvailable.add(d8)
          digitsAvailable.add(d7)
        digitsAvailable.add(d5)
      digitsAvailable.add(d6)
    digitsAvailable.add(d4)
  digitsAvailable.add(d3)
print(ssSum)