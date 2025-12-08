import math

# Read input
with open('input.txt', 'r') as f:
    lines = f.readlines()

positions = []
for line in lines:
    x, y, z = map(int, line.strip().split(','))
    positions.append((x, y, z))

n = len(positions)

# Calculate all pairwise distances
edges = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, z1 = positions[i]
        x2, y2, z2 = positions[j]
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        edges.append((dist, i, j))

edges.sort()

# Union-Find with path compression and union by rank
parent = list(range(n))
rank = [0] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        parent[px] = py
    elif rank[px] > rank[py]:
        parent[py] = px
    else:
        parent[py] = px
        rank[px] += 1
    return True

def count_circuits():
    roots = set()
    for i in range(n):
        roots.add(find(i))
    return len(roots)

# Keep connecting until all boxes are in one circuit
last_connection = None
for dist, i, j in edges:
    if union(i, j):
        circuits = count_circuits()
        last_connection = (i, j)
        if circuits == 1:
            break

# Calculate answer
i, j = last_connection
x1, y1, z1 = positions[i]
x2, y2, z2 = positions[j]
answer = x1 * x2

print(f"Last connection: {positions[i]} <-> {positions[j]}")
print(f"X coordinates: {x1} and {x2}")
print(f"Answer: {answer}")
