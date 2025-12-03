# Day 3: Lobby - Part 2

## Problem Summary

The escalator needs even more power! Now we need to turn on exactly **12 batteries** per bank (instead of 2) to overcome static friction. The joltage is now a 12-digit number formed by the selected batteries.

## Understanding the Problem

The rules are similar to Part 1, but scaled up:
- Must turn on exactly **12 batteries** per bank
- Cannot rearrange batteries (order must be preserved)
- The joltage is the 12-digit number formed by selected batteries
- We want to maximize the joltage from each bank

### Key Insight:
This is equivalent to **selecting 12 digits from a sequence to form the largest possible number** while maintaining their relative order. This is known as the "largest subsequence of length k" problem.

## Approach: Greedy Algorithm with Stack

We use a stack-based greedy approach:

1. **Calculate digits to drop**: `to_drop = total_digits - 12`
2. **Process each digit** from left to right:
   - If current digit is **larger** than the top of stack
   - And we still have digits we can drop
   - **Pop smaller digits** from stack
   - This ensures we keep larger digits early in the sequence
3. **Add current digit** to stack
4. **If we still need to drop more**, remove from the end
5. **Join the stack** to form the final 12-digit number

### Why This Works:
- We greedily keep larger digits towards the front
- We only remove smaller digits when a larger one appears
- This maximizes the numerical value while preserving order

## Example Walkthrough

### Bank: `987654321111111` (15 digits → drop 3)

| Step | Current | Stack | To Drop | Action |
|------|---------|-------|---------|--------|
| 1 | 9 | [9] | 3 | Add 9 |
| 2 | 8 | [9,8] | 3 | Add 8 (8 < 9) |
| 3 | 7 | [9,8,7] | 3 | Add 7 (7 < 8) |
| ... | ... | ... | ... | Continue... |
| End | - | [9,8,7,6,5,4,3,2,1,1,1,1] | 0 | Drop last 3 ones |

**Result**: `987654321111`

### Bank: `234234234234278` (15 digits → drop 3)

Process reveals we should drop the smaller digits at the start (2,3,2) to keep larger digits:
**Result**: `434234234278`

### Bank: `818181911112111` (15 digits → drop 3)

The algorithm identifies that keeping the larger 8s and 9s produces:
**Result**: `888911112111`

## Algorithm Complexity

- **Time**: O(n × m) where n = number of banks, m = average digits per bank
  - Each digit is pushed and popped at most once
- **Space**: O(m) for the stack
- **Much more efficient** than trying all combinations: C(100,12) ≈ 10^12 combinations!

## Comparison with Part 1

| Aspect | Part 1 | Part 2 |
|--------|--------|--------|
| Batteries to select | 2 | 12 |
| Result length | 2 digits | 12 digits |
| Algorithm | Brute force pairs | Greedy stack |
| Complexity | O(m²) | O(m) |
| Example total | 357 | 3,121,910,778,619 |

## Answer

**175053592950232**

This massive number represents the sum of all maximum 12-digit joltages across all battery banks in the input!
