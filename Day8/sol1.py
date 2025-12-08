import math
from collections import defaultdict

def solve():
    # Read junction box positions
    with open('input.txt', 'r') as f:
        positions = []
        for line in f:
            x, y, z = map(int, line.strip().split(','))
            positions.append((x, y, z))
    
    n = len(positions)
    print(f"Number of junction boxes: {n}")
    
    # Calculate all pairwise distances
    # We'll store as (distance, box1_idx, box2_idx)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = positions[i]
            x2, y2, z2 = positions[j]
            # Euclidean distance
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            edges.append((dist, i, j))
    
    print(f"Total possible edges: {len(edges)}")
    
    # Sort edges by distance (shortest first)
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False  # Already in same circuit
        # Union by rank
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1
        return True
    
    # Try the 1000 shortest connections (count attempts, not successes)
    for attempt in range(1000):
        dist, i, j = edges[attempt]
        union(i, j)  # Whether it succeeds or not doesn't matter
    
    # Count circuit sizes
    circuit_members = defaultdict(list)
    for i in range(n):
        root = find(i)
        circuit_members[root].append(i)
    
    # Get circuit sizes
    circuit_sizes = [len(members) for members in circuit_members.values()]
    circuit_sizes.sort(reverse=True)
    
    print(f"Number of circuits: {len(circuit_sizes)}")
    print(f"Top 5 circuit sizes: {circuit_sizes[:5]}")
    
    # Product of three largest
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    
    return result

answer = solve()
print(f"\nAnswer: {answer}")
