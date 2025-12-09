# Day 9 - Part 1: Largest Rectangle Between Red Tiles

## Problem Summary

Given a list of red tile coordinates, find the largest rectangular area that can be formed using any two red tiles as opposite corners.

## Approach

The solution uses a brute force approach to check all possible pairs of red tiles:

1. **Parse Input**: Read coordinates of red tiles from input file
2. **Check All Pairs**: For each pair of red tiles, calculate the rectangular area they would form
3. **Calculate Area**: Area = (width + 1) × (height + 1), where we add 1 to include the endpoints
4. **Track Maximum**: Keep track of the pair that produces the maximum area

## Key Concepts

### Rectangle Area Calculation

For two points (x1, y1) and (x2, y2):

- Width = |x2 - x1| + 1 (inclusive)
- Height = |y2 - y1| + 1 (inclusive)
- Area = Width × Height

### Time Complexity

- **O(n²)** where n is the number of red tiles
- We check all possible pairs: n × (n-1) / 2 comparisons

## Solution Structure

```python
# 1. Read and parse red tile coordinates
# 2. Iterate through all pairs (i, j) where j > i
# 3. Calculate rectangle area for each pair
# 4. Track maximum area and best pair
# 5. Output result
```

## Example

For red tiles at (0, 0), (3, 4), and (5, 2):

- Pair (0,0) and (3,4): Area = 4 × 5 = 20
- Pair (0,0) and (5,2): Area = 6 × 3 = 18
- Pair (3,4) and (5,2): Area = 3 × 3 = 9

Maximum area: **20**

## Result

The solution finds the maximum rectangular area by checking all possible pairs of red tiles and selecting the pair that maximizes the area.
