# Day 3: Lobby - Part 1

## Problem Summary

The elevators are offline due to an electrical surge, and we need to power the escalator using batteries. Each battery bank (line of digits) needs exactly two batteries turned on to produce joltage. Our goal is to maximize the joltage from each bank.

## Understanding the Problem

Each battery is labeled with a joltage rating from 1 to 9. When you turn on exactly two batteries, the joltage produced equals the two-digit number formed by those batteries **in their original order**.

### Key Rules:

- Must turn on exactly **2 batteries** per bank
- Cannot rearrange batteries (order matters)
- The joltage is the number formed by the two selected digits

### Examples:

- Bank `12345`: Turn on batteries at positions 2 and 4 → produces `24` jolts
- Bank `987654321111111`: Turn on positions 1 and 2 → produces `98` jolts (maximum)
- Bank `811111111111119`: Turn on positions 1 and 15 → produces `89` jolts (maximum)

## Approach

Use a brute-force approach to try all possible pairs:

1. **For each battery bank** (line of input)
2. **Try all pairs of positions** (i, j) where i < j
3. **Form the two-digit number** using digits at positions i and j
4. **Track the maximum** joltage found
5. **Sum all maximum joltages** across all banks

### Algorithm Complexity:

- **Time**: O(n × m²) where n = number of banks, m = average digits per bank
- **Space**: O(1) - only storing the running maximum and sum

## Example Walkthrough

Given the example banks:

| Bank              | Best Pair | Max Joltage | Explanation                      |
| ----------------- | --------- | ----------- | -------------------------------- |
| `987654321111111` | (0,1)     | 98          | First two digits: 9 and 8        |
| `811111111111119` | (0,14)    | 89          | First digit 8 and last digit 9   |
| `234234234234278` | (13,14)   | 78          | Last two digits: 7 and 8         |
| `818181911112111` | (6,7)     | 92          | Digits at positions 6,7: 9 and 2 |

**Total**: 98 + 89 + 78 + 92 = **357**

## Solution Strategy

The solution checks every possible pair of batteries systematically:

- For a bank with 15 digits, we check C(15,2) = 105 pairs
- We keep track of the maximum joltage found
- No optimization needed since the search space is small

## Answer

**17554**

This represents the sum of maximum joltages across all battery banks in the input.
