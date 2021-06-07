from math import inf

row = [1]
limit = 1000000
finalRow = 100
numLess = 0
cabooseIndex = inf

for rowNumber in range(1, finalRow+1):
  newRow = [1]
  for k in range(1, min(rowNumber, cabooseIndex+1)):
    newRow.append(row[k] + row[k-1])
    if newRow[-1] > limit:
      cabooseIndex = len(newRow) - 1
      numLess += rowNumber + 1 - 2 * cabooseIndex
      break
  newRow.append(1)
  row = newRow
  rowNumber += 1

print(numLess)