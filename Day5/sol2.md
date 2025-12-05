# Day 5: Cafeteria - Part 2

## Problem Summary

Now we need to count **all** ingredient IDs that the fresh ranges consider to be fresh, not just the available ones. This means counting every single ID covered by the fresh ranges, regardless of what's in inventory.

## Key Difference from Part 1

| Aspect             | Part 1              | Part 2               |
| ------------------ | ------------------- | -------------------- |
| **What to check**  | Available IDs only  | All IDs in ranges    |
| **Second section** | Used (IDs to check) | Ignored (irrelevant) |
| **Count**          | Matching IDs        | Total IDs in ranges  |
| **Example answer** | 3                   | 14                   |

## The Challenge: Overlapping Ranges

**Problem:** Ranges can overlap, and we need to avoid counting IDs twice.

### Example:

```
10-14  (IDs: 10, 11, 12, 13, 14)
12-18  (IDs: 12, 13, 14, 15, 16, 17, 18)
16-20  (IDs: 16, 17, 18, 19, 20)
```

**Naive approach (WRONG):**

- Range 1: 5 IDs
- Range 2: 7 IDs
- Range 3: 5 IDs
- Total: 17 IDs ❌ (IDs 12-14 counted twice, 16-18 counted three times!)

**Correct approach:** Merge overlapping ranges first!

## Solution: Range Merging

### Step 1: Sort Ranges

```
3-5
10-14
12-18
16-20
```

Already sorted by start position.

### Step 2: Merge Overlapping/Adjacent Ranges

Start with first range: `3-5`

**Check `10-14`:**

- Starts at 10, previous ends at 5
- Gap between them (6-9)
- Keep separate: `[3-5]`, `[10-14]`

**Check `12-18`:**

- Starts at 12, previous ends at 14
- Overlaps! (12, 13, 14 are in both)
- Merge: `[3-5]`, `[10-18]`

**Check `16-20`:**

- Starts at 16, previous ends at 18
- Overlaps! (16, 17, 18 are in both)
- Merge: `[3-5]`, `[10-20]`

### Final Merged Ranges:

- `3-5`: 3, 4, 5 → **3 IDs**
- `10-20`: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 → **11 IDs**
- **Total: 14 IDs** ✓

## Algorithm

```python
def merge_overlapping_ranges(ranges):
    # Sort by start position
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # Check if overlapping or adjacent
        if start <= last_end + 1:
            # Merge by extending the end
            merged[-1] = (last_start, max(last_end, end))
        else:
            # No overlap, keep separate
            merged.append((start, end))

    return merged

def count_total_fresh_ids(ranges):
    merged = merge_overlapping_ranges(ranges)

    total = 0
    for start, end in merged:
        total += (end - start + 1)  # +1 because range is inclusive

    return total
```

## Why Adjacent Ranges Matter

We also merge **adjacent** ranges (separated by 1):

```
5-10
11-15
```

These should merge to `5-15` because they're continuous (10 + 1 = 11).

Check: `if start <= last_end + 1`

## Algorithm Complexity

- **Time**: O(n log n) where n = number of ranges
  - Sorting: O(n log n)
  - Merging: O(n)
- **Space**: O(n) for storing ranges

Much more efficient than enumerating every ID!

## Visual Example

**Before merging:**

```
      3-5
           10-14
              12-18
                 16-20
```

**After merging:**

```
      3-5
           10-----------------20
```

**Count:**

- Range 1: 5 - 3 + 1 = 3 IDs
- Range 2: 20 - 10 + 1 = 11 IDs
- **Total: 14 IDs**

## Answer

**333,892,124,923,577**

This enormous number represents all ingredient IDs that the cafeteria's fresh ranges consider to be fresh. The ranges in the input cover a massive span of ID values!

### Insight:

The answer is in the **hundreds of trillions**, showing that the fresh ranges cover extensive ID ranges - likely representing a comprehensive inventory system that's been running for a very long time.
