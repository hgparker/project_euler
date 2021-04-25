import numpy as np

monopoly = np.zeros((40, 40))

diceSides = 4
rollProbability = 1 / (diceSides ** 2)
backgroundDoublesProbability = rollProbability

GO = 0
JAIL = 10
G2J = 30

CC1 = 2
CC2 = 17
CC3 = 33

CH1 = 7
CH2 = 22
CH3 = 36

C1 = 11
E3 = 24
H2 = 39
R1 = 5
R2 = 15
R3 = 25
R4 = 35
U1 = 12
U2 = 18

communityJailProbability = 1/16
communityGoProbability = 1/16
communityNothingProbability = 14/16

chanceNothingProbability = 6/16
chanceGoProbability = 1/16
chanceJailProbability = 1/16
chanceC1Probability = 1/16
chanceE3Probability = 1/16
chanceH2Probability = 1/16
chanceR1Probability = 1/16
chanceNextRProbability = 2/16
chanceNextUProbability = 1/16
chanceBack3Probability = 1/16

for start in range(40):

  # We can't start on this square
  if start == G2J: continue
  
  for die1 in range(1, diceSides+1):
    for die2 in range(1, diceSides+1):
      # Probability of any basic dice combination
      backgroundProbability = rollProbability

      if die1 == die2:
        # We send to jail based on probability of past two rolls having been doubles
        monopoly[start][JAIL] += backgroundDoublesProbability * backgroundProbability
        backgroundProbability *= 1 - backgroundDoublesProbability
        # Having accounted for this, we now adjust the background probability so we don't overcount

      newSquare = (start + die1 + die2) % 40

      if newSquare == G2J:
        # If land on G2J, go to jail
        monopoly[start][JAIL] += backgroundProbability
      elif newSquare == CC1 or newSquare == CC2 or newSquare == CC3:
        # if land on Community Chest, tip it out to JAIL and GO
        monopoly[start][newSquare] += backgroundProbability * communityNothingProbability
        monopoly[start][JAIL] += backgroundProbability * communityJailProbability
        monopoly[start][GO] += backgroundProbability * communityGoProbability
      elif newSquare == CH1 or newSquare == CH2 or newSquare == CH3:
        # if land on Chance, tip it out to JAIL, GO, C1, E3, H2, R1
        monopoly[start][newSquare] += backgroundProbability * chanceNothingProbability
        monopoly[start][GO] += backgroundProbability * chanceGoProbability
        monopoly[start][JAIL] += backgroundProbability * chanceJailProbability
        monopoly[start][C1] += backgroundProbability * chanceC1Probability
        monopoly[start][E3] += backgroundProbability * chanceE3Probability
        monopoly[start][H2] += backgroundProbability * chanceH2Probability
        monopoly[start][R1] += backgroundProbability * chanceR1Probability
        # account for nextR and nextU cards
        if newSquare == CH1:
          nextR = R2
          nextU = U1
        elif newSquare == CH2:
          nextR = R3
          nextU = U2
        elif newSquare == CH3:
          nextR = R1
          nextU = U1
        monopoly[start][nextR] += backgroundProbability * chanceNextRProbability
        monopoly[start][nextU] += backgroundProbability * chanceNextUProbability
        # handle the go back three for CH1 and CH2
        if newSquare == CH1 or newSquare == CH2:
          monopoly[start][newSquare-3] += backgroundProbability * chanceBack3Probability
        else:
          # handle back three for CH3 == CC3
          monopoly[start][CC3] += backgroundProbability * chanceBack3Probability * communityNothingProbability
          monopoly[start][JAIL] += backgroundProbability * chanceBack3Probability * communityJailProbability
          monopoly[start][GO] += backgroundProbability * chanceBack3Probability * communityGoProbability
      else:
        # newSquare isn't anything special, just update probability
        monopoly[start][newSquare] += backgroundProbability

# Diagonalize monopoly matrix
eigenvalues, eigenvectors = np.linalg.eig(monopoly)
future = np.real(np.matmul(np.matmul(eigenvectors, np.diag(eigenvalues ** 1000000)), np.linalg.inv(eigenvectors)))

# Get top three
vals = []
for k in range(40):
  vals.append((k, future[0][k]))
print(sorted(vals, key=lambda x: -x[1])[:3])