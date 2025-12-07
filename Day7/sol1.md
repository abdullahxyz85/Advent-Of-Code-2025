# Day 7: Laboratories - Part 1

## The Adventure Continues

After escaping the trash compactor (thanks, friendly cephalopods!), I found myself in the research wing of the North Pole. And of course, there's a big shiny teleporter just sitting there. Who could resist? I stepped onto it and... uh oh. Wrong move.

Now I'm stuck in an unfamiliar room with a broken teleporter leaking magic smoke. The diagnostic tool helpfully displays error code **0H-N0** (oh no, indeed!), which apparently means there's an issue with one of the tachyon manifolds. Time to fix it!

## The Problem

I found a diagram of the tachyon manifold - my puzzle input. Here's how it works:

- A tachyon beam enters at position **S**
- Tachyon beams **always move downward** (that's their nature)
- They pass freely through empty space (**.**)
- When a beam hits a **splitter (^)**, something interesting happens:
  - The original beam stops
  - Two new beams are emitted from the **immediate left and right** of the splitter
  - Both new beams also move downward

### Example Visualization

```
.......S.......    Start: beam enters at S
.......|.......    Beam moves down
......|^|......    Hits splitter! Creates left & right beams
......|.|......    Both continue down
.....|^|^|.....    More splits!
```

After all the splitting is done, the example shows **21 total splits**.

## Understanding the Physics

The key insight here is understanding what happens at a splitter:

1. **Original beam stops** - it doesn't continue through the splitter
2. **Two new beams spawn** - one at `(splitter_row, splitter_col - 1)` and one at `(splitter_row, splitter_col + 1)`
3. **Both move downward** - they don't move sideways, just down like all tachyon beams

So if a beam at column 7 hits a splitter at row 5, column 7:

- The beam at (4, 7) stops
- New beam starts at (5, 6) moving down
- New beam starts at (5, 8) moving down

## My Approach

I used a **BFS (Breadth-First Search)** approach to simulate the beams:

1. **Initialize**: Start with one beam at position S
2. **Process each beam**:
   - Move it down one row
   - Check what's at the next position
   - If it's a splitter (^): increment split counter and create two new beams
   - If it's empty (.): continue the beam downward
   - If it exits the grid: beam is done
3. **Track visited positions** to avoid processing the same beam twice
4. **Count the splits**

## The Algorithm

```python
def solve():
    # Find starting position S
    start_row, start_col = find_S(grid)

    # Track beams as (row, col)
    beams = [(start_row, start_col)]
    visited = set()
    split_count = 0

    while beams:
        row, col = beams.pop(0)

        if (row, col) in visited:
            continue
        visited.add((row, col))

        # Move beam downward
        next_row, next_col = row + 1, col

        # Check if beam exits
        if next_row >= len(grid):
            continue

        next_char = grid[next_row][next_col]

        if next_char == '^':
            # SPLIT! Count it and create two new beams
            split_count += 1
            beams.append((next_row, next_col - 1))  # Left beam
            beams.append((next_row, next_col + 1))  # Right beam
        elif next_char == '.':
            # Continue downward
            beams.append((next_row, next_col))

    return split_count
```

## Complexity

- **Time**: O(R × C) where R = rows, C = columns
  - In worst case, we might visit every cell once
- **Space**: O(R × C) for the visited set and beam queue

Pretty efficient for a quantum physics problem! 😄

## Common Pitfalls I Avoided

1. **Don't move beams sideways!** - I initially thought beams moved left/right after splitting, but they only move down
2. **Beams spawn NEXT to splitters** - not on top of them
3. **Track visited positions** - without this, you might process the same beam path multiple times
4. **Check bounds carefully** - make sure new beams are within grid boundaries

## The Answer

After simulating all the beam splitting in my manifold:

**Answer: 1,698**

That's a lot of splits! But now I know exactly what's happening in the manifold. Time for Part 2... 🔬

## Key Takeaways

- **Physics simulations are fun** - even when they're about fictional tachyon beams
- **BFS is your friend** - great for exploring all possible paths
- **Read the problem carefully** - the detail about beams spawning "immediately left and right" was crucial
- **Visualize the problem** - drawing out the example helped me understand the beam behavior

Now let's see what this quantum tachyon manifold has in store... ⚛️
