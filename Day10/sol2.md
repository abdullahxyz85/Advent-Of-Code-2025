# Day 10 Part 2: Joltage Configuration

## Problem Summary

Now we need to configure joltage counters instead of indicator lights. Each machine has:

- Multiple counters (initially all at 0)
- Target joltage values (shown in braces like `{3,5,4,7}`)
- Buttons that increment specific counters (shown in parentheses like `(1,3)`)

The goal is to find the minimum total button presses needed to configure all machines' counters to reach their target values.

## Solution Approach

This is a **system of linear equations over non-negative integers**, where:

- Each counter value is the sum of all button presses affecting it
- Each button can be pressed any non-negative number of times
- We want to minimize the total number of button presses

### Key Differences from Part 1

1. **Addition instead of XOR**: Counters increment (not toggle)
2. **Integer values**: Each button press adds 1 (not toggle between 0 and 1)
3. **Multiple presses**: Buttons can be pressed more than once
4. **Linear system**: Solve A·x = b where x_i ≥ 0 and x_i ∈ ℤ

### Algorithm

I used **Gaussian elimination with rational arithmetic**:

1. **Parse input**: Extract target joltages and button definitions
2. **Build augmented matrix [A|b]**:
   - Each row represents one counter equation
   - Each column represents one button variable
   - A[i][j] = 1 if button j affects counter i
   - b[i] = target value for counter i
3. **Gaussian elimination**: Reduce to row echelon form using Fraction for exact arithmetic
4. **Extract solution**: Read off button press counts from reduced matrix
5. **Handle underdetermined systems**: Use greedy approach to find minimum norm solution

### Example

For `{3,5,4,7}` with buttons `(3) (1,3) (2) (2,3) (0,2) (0,1)`:

- Counter 0: x₅ + x₆ = 3
- Counter 1: x₂ + x₆ = 5
- Counter 2: x₃ + x₄ + x₅ = 4
- Counter 3: x₁ + x₂ + x₄ = 7
- Minimum: 10 presses (one solution: press button 1 once, button 2 three times, button 4 three times, button 5 once, button 6 twice)

## Answer

**20750** total button presses required for all machines

## Implementation Notes

- Used `fractions.Fraction` for exact rational arithmetic during Gaussian elimination
- Handled both determined and underdetermined systems
- Greedy fallback for cases where standard elimination doesn't give integer solution
- Verified all solutions before returning
