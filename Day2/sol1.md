# Day 2: Gift Shop - Part 1

## Problem Summary

A young Elf accidentally added invalid product IDs to the gift shop database. Our task is to identify and sum all invalid IDs within given ranges.

## What Makes an ID Invalid?

An ID is invalid if it's made of a sequence of digits repeated **exactly twice**.

### Examples:

- `55` → "5" repeated twice ✓
- `6464` → "64" repeated twice ✓
- `123123` → "123" repeated twice ✓
- `111` → "1" repeated three times ✗ (not exactly twice)

### Important Note:

Numbers with leading zeros aren't valid IDs. For example, `0101` isn't considered an ID at all.

## Approach

1. **Parse the input**: Split ranges by commas, each range formatted as `start-end`
2. **Check each number** in every range to see if it matches the pattern
3. **Validate the pattern**:
   - Must have even length (to split into two equal halves)
   - First half must equal second half
   - No leading zeros in the pattern
4. **Sum all invalid IDs** found across all ranges

## Example Walkthrough

Given ranges like `11-22,95-115,998-1012`:

- **11-22**: Found `11` and `22` (both invalid)
- **95-115**: Found `99` (9 repeated twice)
- **998-1012**: Found `1010` (10 repeated twice)

## Solution Complexity

- **Time**: O(n × m) where n is the total numbers in all ranges and m is the average number length
- **Space**: O(1) - only storing the running sum

## Answer

**28146997880**

Found 816 invalid IDs across all input ranges.
