# Day 9 - Part 2: Largest Valid Rectangle with Red/Green Tiles

## Problem Summary

Find the largest rectangle with red tile corners that contains ONLY red and green tiles. Red tiles form a closed loop connected by straight lines of green tiles, and all tiles inside the loop are also green.

## Key Constraints

1. Rectangle must have red tiles at opposite corners
2. ALL tiles in the rectangle must be either red or green (on boundary or inside the polygon)
3. No tiles outside the polygon are allowed in the rectangle

## Approach

### 1. Build the Boundary

- Red tiles form vertices of a polygon
- Connect consecutive red tiles with horizontal/vertical lines of green tiles
- These connections form the boundary of the polygon

### 2. Precompute X-Bounds for Each Y-Level

Instead of checking every point with expensive polygon containment tests, we:

- Build horizontal and vertical boundary segments
- For each y-coordinate, compute the valid x-range (min_x to max_x)
- Merge overlapping segments to get continuous bounds

### 3. Efficient Rectangle Validation

For a candidate rectangle (min_x, max_x, min_y, max_y):

- Use binary search to find relevant y-coordinates
- Check strategic y-levels: boundaries, min_y, max_y, and positions just above/below boundaries
- Verify that the rectangle's x-range fits within the valid bounds for each checked y-level

### 4. Optimized Search Strategy

- Generate all candidate pairs of red tiles
- Sort by potential area (descending)
- Validate candidates from largest to smallest
- Return first valid rectangle (guaranteed to be largest)

## Algorithm Components

### `build_boundary_segments`

Analyzes consecutive red tiles to create:

- **Horizontal segments**: Green tiles connecting red tiles on same row
- **Vertical segments**: Green tiles connecting red tiles on same column
- **Boundary y-coordinates**: All y-values where boundaries exist

### `compute_x_bounds_by_y`

For each y-coordinate:

- Collects all x-ranges from horizontal segments at that y
- Adds x-positions from vertical segments crossing that y
- Merges overlapping ranges to get min/max valid x-bounds

### `is_valid_rectangle`

Validates a rectangle efficiently:

- Uses binary search to find relevant boundary y-coordinates
- Checks only strategic y-positions (not every single row)
- Verifies rectangle stays within valid x-bounds at each checked y

### `find_largest_rectangle`

Main search logic:

- Creates list of all candidate pairs with their potential areas
- Sorts by area descending
- Validates from largest to smallest
- Returns immediately when first valid rectangle is found

## Optimization Techniques

### 1. Binary Search (bisect)

- `bisect_left` and `bisect_right` find relevant y-coordinates quickly
- Avoids checking every y-coordinate between min_y and max_y

### 2. Strategic Sampling

Instead of checking every point in rectangle:

- Check y-coordinates at boundaries
- Check y-coordinates just above/below boundaries (y±1)
- Check rectangle's min_y and max_y
- This catches edge cases without exhaustive point checking

### 3. Early Termination

- Sort candidates by area descending
- First valid rectangle found is guaranteed to be largest
- No need to check smaller candidates

### 4. Precomputed Bounds

- X-bounds computed once per y-coordinate
- Reused for all rectangle validations
- O(1) lookup instead of O(n) polygon tests

## Time Complexity

- Building boundary: **O(n)** where n = number of red tiles
- Computing x-bounds: **O(m)** where m = number of unique y-coordinates
- Sorting candidates: **O(n² log n)**
- Validation per rectangle: **O(log m)** using binary search
- Overall: **O(n² log n)** dominated by sorting

## Space Complexity

- **O(n + m)** for storing segments and bounds
- **O(n²)** for candidate pairs list

## Answer

The solution found a valid rectangle with area **197,708**:

- Red tile corners: (96232, 63257) and (96072, 64484)
- Dimensions: 161 × 1,228
- All 197,708 tiles verified to be on boundary or inside polygon
