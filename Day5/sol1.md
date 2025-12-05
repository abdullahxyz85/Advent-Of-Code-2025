# Day 5: Cafeteria - Part 1

## Problem Summary

The cafeteria's new inventory management system tracks ingredient freshness using ID ranges. We need to check which of the available ingredient IDs are actually fresh according to the database.

## Understanding the Problem

The database has two sections separated by a blank line:

1. **Fresh ID ranges** (inclusive ranges like `3-5` means IDs 3, 4, and 5 are fresh)
2. **Available ingredient IDs** (the IDs we need to check)

### Key Rules:

- Ranges are **inclusive**: `3-5` includes 3, 4, and 5
- Ranges can **overlap**: An ID is fresh if it's in ANY range
- We only check the **available IDs** listed in the second section

## Example Walkthrough

**Input:**

```
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

**Analysis:**

| ID  | Ranges Checked           | Status     | Reason                    |
| --- | ------------------------ | ---------- | ------------------------- |
| 1   | 3-5, 10-14, 16-20, 12-18 | ❌ Spoiled | Not in any range          |
| 5   | 3-5, 10-14, 16-20, 12-18 | ✅ Fresh   | In range 3-5              |
| 8   | 3-5, 10-14, 16-20, 12-18 | ❌ Spoiled | Not in any range          |
| 11  | 3-5, 10-14, 16-20, 12-18 | ✅ Fresh   | In range 10-14            |
| 17  | 3-5, 10-14, 16-20, 12-18 | ✅ Fresh   | In ranges 16-20 AND 12-18 |
| 32  | 3-5, 10-14, 16-20, 12-18 | ❌ Spoiled | Not in any range          |

**Result:** 3 fresh ingredients (5, 11, 17)

## Approach

### Step 1: Parse Input

```python
# Split at blank line
ranges_section, ids_section = input.split('\n\n')

# Parse ranges: "3-5" → (3, 5)
ranges = [parse_range(line) for line in ranges_section]

# Parse IDs: "5" → 5
ingredient_ids = [int(line) for line in ids_section]
```

### Step 2: Check Each ID

```python
def is_fresh(ingredient_id, ranges):
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False
```

### Step 3: Count Fresh Ingredients

```python
fresh_count = sum(1 for id in ingredient_ids if is_fresh(id, ranges))
```

## Algorithm Complexity

- **Time**: O(n × m) where:
  - n = number of available IDs to check
  - m = number of ranges
- **Space**: O(n + m) for storing ranges and IDs

## Edge Cases

- **Single ID range**: `5-5` is valid (just ID 5)
- **Overlapping ranges**: ID can be in multiple ranges (still counts as 1 fresh)
- **Large numbers**: IDs can be very large integers
- **No fresh IDs**: All available IDs could be spoiled

## Answer

**525**

Out of all the available ingredient IDs in the database, 525 are fresh according to the defined ranges.
