# Day 8: Playground - Part 1

## Problem Summary

The Elves need to connect junction boxes in the playground using extension cables. Each junction box has 3D coordinates (X, Y, Z). They can only make 1000 connections and want to minimize the number of separate circuits.

The goal is to connect the 1000 closest pairs of junction boxes and find the product of the sizes of the three largest remaining circuits.

## Approach

This is a classic **Minimum Spanning Tree (MST)** problem with a twist - we're limited to 1000 connections rather than connecting everything.

### Algorithm: Kruskal's Algorithm with Union-Find

1. **Parse Input**: Read all 1000 junction box coordinates (X, Y, Z)

2. **Calculate Distances**: Compute Euclidean distance for all possible pairs:

   - Total pairs: 1000 × 999 / 2 = 499,500 edges
   - Distance formula: `sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)`

3. **Sort Edges**: Sort all edges by distance (shortest first)

4. **Union-Find Data Structure**:

   - Track which junction boxes belong to the same circuit
   - Path compression for efficient lookups
   - Union by rank for balanced trees

5. **Process Connections**:

   - Try to connect the 1000 shortest pairs
   - Key insight: Count **attempts**, not successful connections
   - Some connections fail because boxes are already in the same circuit

6. **Find Answer**:
   - Count the size of each remaining circuit
   - Multiply the three largest circuit sizes

## Key Insight

The problem asks for "the first 1000 connections" which means the first 1000 **attempts** from the sorted edge list, regardless of whether the connection succeeds (boxes in different circuits) or fails (already connected). This is different from making exactly 1000 successful connections.

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

# Process the first 1000 connection attempts
for attempt in range(1000):
    dist, i, j = edges[attempt]
    union(i, j)

# Count circuit sizes
from collections import defaultdict
circuit_sizes = defaultdict(int)
for i in range(n):
    root = find(i)
    circuit_sizes[root] += 1

# Get top 3 circuit sizes
sizes = sorted(circuit_sizes.values(), reverse=True)
answer = sizes[0] * sizes[1] * sizes[2]
```

## Result

- **1000 junction boxes** processed
- **499,500 total possible edges** calculated
- **1000 shortest connection attempts** made
- **278 circuits remaining**
- **Top 3 circuit sizes**: 52, 43, 38

**Answer: 84,968** (52 × 43 × 38)

## Complexity

- **Time**: O(n² log n) for calculating and sorting all edges
- **Space**: O(n²) for storing all edges
- **Union-Find operations**: Nearly O(1) with path compression and union by rank
