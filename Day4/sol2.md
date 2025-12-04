# Day 4: Printing Department - Part 2

## Problem Summary

Now we need to simulate the **cascading removal process**. Once accessible rolls are removed, more rolls may become accessible. The question is: how many total rolls can be removed if we keep repeating this process until no more rolls can be accessed?

## Understanding the Cascading Effect

When we remove a roll from the grid:

1. It creates empty space (`.`)
2. Its neighbors now have one fewer adjacent roll
3. Some neighbors might now have **< 4 adjacent rolls** and become accessible
4. This creates a chain reaction or "cascade"

## Process Simulation

The removal happens in rounds:

### Round 1: Initial State

Find and remove all rolls with < 4 adjacent rolls.

### Round 2: After First Removal

- Grid has changed (some `@` became `.`)
- Remaining rolls may now have fewer neighbors
- Find and remove newly accessible rolls

### Continue...

Repeat until no more rolls can be removed.

## Example Walkthrough

Using the example grid:

| Round     | Rolls Removed | Cumulative Total |
| --------- | ------------- | ---------------- |
| 1         | 13            | 13               |
| 2         | 12            | 25               |
| 3         | 7             | 32               |
| 4         | 5             | 37               |
| 5         | 2             | 39               |
| 6         | 1             | 40               |
| 7         | 1             | 41               |
| 8         | 1             | 42               |
| 9         | 1             | 43               |
| **Total** | **43**        | -                |

### Why the Cascade Happens:

**Initial:** Dense cluster with many rolls having 4+ neighbors (inaccessible)

```
@@@@@
@@@@@
@@@@@
```

**After removing edge rolls:** Interior rolls now have fewer neighbors

```
..@..
.@@@.
..@..
```

**Continue:** More rolls become accessible as neighbors are removed

## Approach

1. **Copy the grid** (we'll be modifying it)
2. **While accessible rolls exist:**
   - Find all currently accessible rolls (< 4 neighbors)
   - Remove them all simultaneously (replace `@` with `.`)
   - Increment total count
3. **Return total removed**

### Key Implementation Details:

- **Simultaneous removal**: Find ALL accessible rolls first, then remove them together
- **Grid modification**: Each removal changes the state for the next iteration
- **Termination**: Loop ends when `find_accessible_rolls()` returns empty list

## Algorithm Complexity

- **Time**: O(k × n × m) where:
  - k = number of rounds (worst case: number of rolls)
  - n × m = grid dimensions
- **Space**: O(n × m) for the grid copy

In practice, k is much smaller than total rolls because many are removed simultaneously.

## Comparison with Part 1

| Aspect         | Part 1           | Part 2              |
| -------------- | ---------------- | ------------------- |
| Operation      | Count accessible | Remove all possible |
| Grid state     | Static           | Dynamic (modified)  |
| Iterations     | 1 pass           | Multiple rounds     |
| Answer type    | Snapshot count   | Cumulative total    |
| Example result | 13               | 43                  |

## Visual Example

**Start → Round 1 → Round 2 → ... → Final**

The grid progressively empties from the edges inward, as the cascade effect "peels away" layers of rolls.

## Answer

**8538**

This represents the total number of paper rolls that can be removed through the complete cascading process, helping the Elves clear as much space as possible in the printing department!

### Insight:

The difference between Part 1 (1508) and Part 2 (8538) shows that the cascading effect removes **5.66× more rolls** than what's initially accessible!
