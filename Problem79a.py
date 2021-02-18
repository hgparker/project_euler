# Method 1...topological sort

f = open("Problem79_input", "r")
data = []
for k in range(50):
  data.append(f.readline().strip())
f.close()

edges = {} # v
nodes = set()

for datum in data:
  for c in datum:
    nodes.add(c)
  if datum[0] not in edges:
    edges[datum[0]] = {datum[1]}
  else:
    edges[datum[0]].add(datum[1])
  if datum[1] not in edges:
    edges[datum[1]] = {datum[2]}
  else:
    edges[datum[1]].add(datum[2])

visited = set()
stack = []

def dfs(node):
  visited.add(node)
  if node in edges:
    for downstream in edges[node]:
      if downstream not in visited:
        dfs(downstream)
  stack.append(node)

for node in nodes:
  if not node in visited:
    dfs(node)

print("".join(stack[::-1]))