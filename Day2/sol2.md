# Day 2: Gift Shop - Part 2

## Problem Summary

Turns out the Elf was doing more silly patterns! Now we need to find IDs that are made of a sequence repeated **at least twice** (not just exactly twice).

## What Makes an ID Invalid? (Updated Rules)

An ID is invalid if it consists of any pattern repeated **2 or more times**.

### Examples:

- `12341234` → "1234" repeated 2 times ✓
- `123123123` → "123" repeated 3 times ✓
- `1212121212` → "12" repeated 5 times ✓
- `1111111` → "1" repeated 7 times ✓
- `111` → "1" repeated 3 times ✓ (now invalid!)
- `999` → "9" repeated 3 times ✓ (now invalid!)

## Key Differences from Part 1

Part 1 only caught patterns repeated exactly twice. Part 2 catches patterns repeated 2+ times, meaning:

- Single digit patterns like `111`, `999`, `7777` are now invalid
- Patterns repeated 3, 4, 5+ times are now caught
- All Part 1 invalid IDs are still invalid in Part 2

## Approach

1. **For each number**, try all possible pattern lengths (1 to half the number's length)
2. **For each pattern length**:
   - Extract the pattern (first n digits)
   - Check if repeating this pattern creates the entire number
   - Verify the pattern has no leading zeros
   - Confirm it repeats at least 2 times
3. **Return true** if any valid repeating pattern is found
4. **Sum all invalid IDs** across all ranges

## Example Differences

Comparing the same ranges with Part 1:

| Range               | Part 1 Invalid IDs | Part 2 Invalid IDs |
| ------------------- | ------------------ | ------------------ |
| 11-22               | 11, 22             | 11, 22             |
| 95-115              | 99                 | 99, 111            |
| 998-1012            | 1010               | 999, 1010          |
| 565653-565659       | (none)             | 565656             |
| 824824821-824824827 | (none)             | 824824824          |

Notice how Part 2 finds additional invalid IDs like `111` (1×3), `999` (9×3), `565656` (565×2), and `824824824` (824×3).

## Solution Complexity

- **Time**: O(n × m²) where n is total numbers and m is average number length (checking all pattern lengths)
- **Space**: O(m) for storing the number as a string

## Answer

**40028128307**

This includes all invalid IDs with patterns repeated 2 or more times.
