# Day 8: Playground - Part 2

## Problem Summary

The Elves realize they don't have enough extension cables with just 1000 connections. Now they need to keep connecting junction boxes until **all 1000 boxes form a single circuit**.

The goal is to find the last connection needed to unify everything, then multiply the X coordinates of those two junction boxes.

## Approach

This is the completion of **Kruskal's Minimum Spanning Tree** algorithm - we continue from Part 1 until we have exactly one connected component.

### Algorithm: Complete MST with Union-Find

1. **Same Setup as Part 1**:

   - Parse 1000 junction box coordinates
   - Calculate all 499,500 pairwise distances
   - Sort edges by distance

2. **Union-Find with Circuit Counting**:

   - Same efficient Union-Find structure
   - Add a function to count remaining circuits
   - Track the last successful connection

3. **Connect Until One Circuit**:

   - Process edges in order of increasing distance
   - Only make connections between boxes in different circuits
   - Stop when circuit count reaches 1

4. **Calculate Answer**:
   - Get the X coordinates of the last two boxes connected
   - Multiply them together

## Mathematical Properties

For **n** junction boxes to form a single connected tree:

- Exactly **n-1** edges are needed
- For 1000 boxes: **999 successful connections** required
- Failed connection attempts (boxes already in same circuit) don't count toward this total

## Solution Code

```python
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
```

## Result

- **999 successful connections** made (as expected for 1000 nodes)
- **Last connection**: (94118, 14262, 86867) ↔ (92049, 7915, 99919)
- **X coordinates**: 94118 and 92049
- **Final state**: All junction boxes in 1 circuit

**Answer: 8,663,467,782** (94118 × 92049)

## Why This Works

The Union-Find algorithm efficiently:

- Prevents cycles (redundant connections)
- Maintains a forest of trees that gradually merge
- Guarantees the minimum total cable length (MST property)
- Knows exactly when we've achieved full connectivity

The last connection is always the one that reduces the circuit count from 2 to 1, completing the spanning tree.

## Complexity

- **Time**: O(n² log n) dominated by sorting edges
- **Space**: O(n²) for edge list
- **Union-Find**: Nearly O(1) per operation with optimizations
- **Circuit counting**: O(n) but only called when connection succeeds
