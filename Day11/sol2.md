# Day 11 - Part 2: Reactor Path Finding with Required Nodes

## Problem Summary

Find all paths from "svr" to "out" that must visit both "dac" and "fft" (in any order).

## Approach

Enhanced DFS with memoization to handle the large number of paths efficiently.

### Key Optimizations

1. **Memoization**: Cache results for (node, visited_required_nodes) states
2. **Frozensets**: Use immutable sets for hashable memoization keys
3. **State Tracking**: Only track which required nodes have been visited, not the full path

### Algorithm

1. Start DFS from "svr"
2. Track visited nodes to avoid cycles
3. Track which required nodes (dac, fft) have been visited
4. At "out", count only if both required nodes were visited
5. Use memoization to avoid recalculating subproblems

## Example Verification

✅ Example test: **2 paths** (matches expected)

The example has 8 total paths from svr to out, but only 2 visit both dac and fft:

- svr → aaa → fft → ccc → eee → dac → fff → ggg → out
- svr → aaa → fft → ccc → eee → dac → fff → hhh → out

## Answer

**533996779677200**

The optimization makes the solution run instantly instead of taking hours!
