# Day 4: Printing Department - Part 1

## Problem Summary

The printing department has rolls of paper (`@`) scattered on a large grid, and forklifts need to access them. However, forklifts can only reach rolls that aren't too crowded - specifically, rolls with **fewer than 4** adjacent rolls.

## Understanding the Problem

Each roll of paper is represented by `@` on a grid. For each roll, we need to check its 8 adjacent positions (horizontal, vertical, and diagonal neighbors).

### Accessibility Rule:

A roll can be accessed by a forklift if it has **fewer than 4 rolls** in its 8 surrounding positions.

### The 8 Adjacent Positions:

```
NW  N  NE
 W  @  E
SW  S  SE
```

## Examples

### Example Grid:

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

**Accessible rolls (marked with `x`):**

```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

In this example, **13 rolls** are accessible:

- Corner rolls with few neighbors
- Edge rolls with open space
- Isolated rolls not surrounded by 4+ other rolls

## Approach

1. **Parse the grid** from input file
2. **For each cell containing `@`:**
   - Count adjacent cells (all 8 directions) that also contain `@`
   - If count < 4, the roll is accessible
3. **Count total accessible rolls**

### Algorithm Complexity:

- **Time**: O(n × m) where n and m are grid dimensions
  - Each cell checked once
  - Each check examines 8 neighbors (constant time)
- **Space**: O(n × m) for storing the grid

## Code Structure

```python
def count_adjacent_rolls(grid, row, col):
    # Check all 8 directions
    # Return count of adjacent @ symbols

def find_accessible_rolls(grid):
    # Iterate through grid
    # Count rolls with < 4 neighbors
    # Return total count
```

## Edge Cases

- **Corner positions**: Have only 3 possible neighbors
- **Edge positions**: Have only 5 possible neighbors
- **Isolated rolls**: Have 0 neighbors (always accessible)
- **Completely surrounded rolls**: Can have up to 8 neighbors

## Answer

**1508**

This represents the total number of paper rolls that forklifts can immediately access in the printing department grid.
