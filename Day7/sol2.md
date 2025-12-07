# Day 7: Laboratories - Part 2

## The Quantum Plot Twist

Just when I thought I understood the manifold, I opened up the teleporter and discovered something mind-blowing: this isn't a _classical_ tachyon manifold - it's a **quantum** tachyon manifold! 🤯

Instead of multiple beams traveling through the manifold independently, there's only **one single tachyon particle** that exists in a quantum superposition. When it reaches a splitter, it takes **BOTH** paths simultaneously!

## Welcome to the Many-Worlds Interpretation

Since a particle can't actually be in two places at once (or can it? 🤔), the manual explains using the **many-worlds interpretation**:

- Each time a particle hits a splitter, **time itself splits**
- In one timeline, the particle went left
- In another timeline, the particle went right
- Both timelines are equally real!

The question: **How many different timelines exist after the particle completes all possible journeys?**

## Understanding Timelines

A timeline is basically a unique path from S to the bottom of the manifold. Let me trace through some possibilities:

### Timeline 1: Always Go Left

```
.......S.......
.......|.......
......|^.......    Take left path
......|........
.....|^.^......    Take left again
.....|.........
....|^.^.^.....    Keep going left
```

### Timeline 2: Alternate Left and Right

```
.......S.......
.......|.......
......|^.......    Take left
......|........
......^|^......    But now take right!
.......|.......
.....^|^.^.....
```

Each unique sequence of left/right choices creates a different timeline. In the example, there are **40 different timelines**.

## Why Not 2^21?

In Part 1, we had 21 splits. You might think 2^21 = 2,097,152 timelines (since each split gives 2 choices). But that's way more than 40!

The key is that **many paths converge**. Different sequences of left/right choices can lead to the same final position, but they're counted as the same timeline endpoint. What we're counting is distinct final positions weighted by the number of ways to reach them.

## My First Attempt (Failed)

I tried using DFS to enumerate all unique paths:

```python
def count_paths_dfs(row, col, path):
    # Store complete path
    if exits_manifold:
        timelines.add(tuple(path))  # Store full path
```

**Problem**: This was too slow and memory-intensive! With 95+ trillion paths, storing each full path is impossible.

## The Better Approach: Dynamic Programming

Instead of tracking complete paths, I track **how many paths reach each position**:

```python
paths_count[(row, col)] = number of distinct ways to reach this cell
```

Here's the beautiful insight:

- If 5 paths reach position A
- And A splits into positions B and C
- Then 5 paths reach B, and 5 paths reach C

We process row by row, propagating the path counts downward!

## The Algorithm

```python
def solve():
    from collections import defaultdict

    paths_count = defaultdict(int)
    paths_count[(start_row, start_col)] = 1  # One path to start

    # Process each row from top to bottom
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if paths_count[(row, col)] == 0:
                continue

            count = paths_count[(row, col)]
            next_row = row + 1

            if next_row >= len(grid):
                continue

            next_char = grid[next_row][col]

            if next_char == '^':
                # Quantum split! Particle takes BOTH paths
                paths_count[(next_row, col - 1)] += count  # Left
                paths_count[(next_row, col + 1)] += count  # Right
            elif next_char == '.':
                # Continue downward
                paths_count[(next_row, col)] += count

    # Sum all paths that reached the bottom row
    total = sum(paths_count[(last_row, col)] for col in range(width))
    return total
```

## Visual Example

Let's trace a simple case:

```
  S      paths_count[(0,1)] = 1
  |
  ^      Splitter at (1,1)
 / \
.   .    paths_count[(2,0)] = 1, paths_count[(2,2)] = 1
|   |
^   ^    Both split again!
```

Each position tracks how many timelines pass through it.

## Complexity

- **Time**: O(R × C) - we visit each cell once
- **Space**: O(R × C) - store counts for positions that have paths
- **Much better than**: O(2^splits) which would be exponential!

## The Difference from Part 1

| Aspect        | Part 1                     | Part 2                  |
| ------------- | -------------------------- | ----------------------- |
| **Concept**   | Multiple independent beams | Single quantum particle |
| **Splitting** | Creates 2 new beams        | Creates 2 timelines     |
| **Goal**      | Count total splits         | Count total timelines   |
| **Answer**    | 1,698                      | 95,408,386,769,474      |
| **Approach**  | BFS simulation             | Dynamic programming     |

## The Answer

After applying the many-worlds interpretation:

**Answer: 95,408,386,769,474**

That's over **95 TRILLION timelines**! 🌌

In every single one of those timelines, a version of me is fixing this teleporter. Some of them are probably doing it faster than me. Thanks, quantum mechanics!

## Key Insights

1. **Path counting ≠ Path enumeration** - Don't store every path, just count them
2. **Dynamic programming is powerful** - Turn exponential into linear
3. **Quantum mechanics is weird** - But computationally interesting!
4. **Big numbers are big** - 95 trillion is a lot of parallel universes
5. **Convergence matters** - Many paths lead to the same destination

## Philosophical Takeaway

Somewhere in one of those 95 trillion timelines, I made different choices and am probably not stuck in a teleporter room right now. But in THIS timeline, at least I get to solve cool puzzles! 🎯

_Note to self: Maybe test teleporters BEFORE stepping on them next time..._
