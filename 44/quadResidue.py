
# Finds two solutions with quadratic residue of -1
# Note that m must be product of prime powers of form 4k+1


# Method1 : Brute force...O(m)

def getQuadraticResidue(m):
  for r in range(m):
    if (r ** 2) % m == m-1:
      return (r, m-r)
  
# For later
# Method2 : (a) resolve to prime powers, (b) get brute force solution for those, (c) combine with Chinese Remainder Theorem
# Method3 : Tonelli-Shanks