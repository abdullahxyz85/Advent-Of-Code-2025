# Day 11 - Part 1: Reactor Path Finding

## Problem Summary

Find all distinct paths from the device labeled "you" to the device labeled "out" in a directed graph representing electrical conduits in a reactor.

## Approach

This is a classic **graph path counting problem** solved using **Depth-First Search (DFS)** with backtracking.

### Algorithm

1. **Parse Input**: Build an adjacency list representation of the directed graph
2. **DFS with Backtracking**:
   - Start from "you" node
   - Explore all possible paths recursively
   - Track visited nodes to avoid cycles
   - Count paths that reach "out"
   - Backtrack by unmarking visited nodes after exploring

### Key Insights

- Each device can have multiple outputs (edges in the graph)
- Data flows only in one direction (directed graph)
- Need to avoid cycles by tracking visited nodes
- Backtracking allows counting all distinct paths

## Example

```
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
```

Paths from "you" to "out":

1. you → bbb → ddd → ggg → out
2. you → bbb → eee → out
3. you → ccc → ddd → ggg → out
4. you → ccc → eee → out
5. you → ccc → fff → out

Total: **5 paths**

## Solution Verification

✅ Example test: 5 paths (matches expected)
✅ Actual puzzle: **683 paths**

## Answer

**683**
