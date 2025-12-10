# Day 10 Part 1: Factory Initialization

## Problem Summary

We need to configure indicator lights on factory machines by pressing buttons. Each machine has:

- Indicator lights (initially all off)
- A target configuration (shown in brackets like `[.##.]`)
- Buttons that toggle specific lights (shown in parentheses like `(0,2,3)`)

The goal is to find the minimum total button presses needed to configure all machines.

## Solution Approach

This problem is a **system of linear equations over GF(2)** (binary field), where:

- Each light state is 0 (off) or 1 (on)
- Each button press toggles certain lights
- We need to find which buttons to press (and how many times)

### Key Insights

1. Pressing a button twice returns lights to original state, so we only need to consider pressing each button 0 or 1 times
2. The problem reduces to: for each light, the XOR of all button presses affecting it must equal the target state
3. This forms a system of linear equations modulo 2

### Algorithm

I used **Gaussian elimination over GF(2)** to solve the system:

1. **Parse input**: Extract target configuration and button definitions
2. **Build matrix**: Create augmented matrix where:
   - Each row represents one light
   - Each column represents one button
   - Matrix[i][j] = 1 if button j toggles light i
   - Last column is the target state for each light
3. **Row reduction**: Use Gaussian elimination with operations modulo 2
4. **Back substitution**: Find which buttons to press
5. **Count presses**: Sum the solution vector

### Example

For `[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1)`:

- Target: [0,1,1,0]
- Buttons toggle: {3}, {1,3}, {2}, {2,3}, {0,2}, {0,1}
- Minimum: 2 presses (buttons 5 and 6: `(0,2)` and `(0,1)`)

## Answer

**535** total button presses required for all machines

## Implementation Notes

- Used modulo 2 arithmetic for all operations
- Gaussian elimination handles redundant/dependent button configurations
- Time complexity: O(n³) where n is number of buttons per machine
