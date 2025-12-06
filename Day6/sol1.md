# Day 6: Trash Compactor - Part 1

## The Story

So here I am, jumped into a garbage chute (because apparently that's what we do for fun now), and ended up in a trash compactor. While some friendly cephalopods are working on getting me out, the youngest one needs help with math homework. Sure, why not? What else am I going to do while waiting?

## The Problem

The math worksheet looks... weird. Instead of problems written left-to-right like we're used to, cephalopods arrange their problems vertically! Each problem is a column of numbers with an operator at the bottom.

### Example Worksheet

```
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
```

This actually represents **four separate problems**:

- **Problem 1**: `123 * 45 * 6 = 33,210`
- **Problem 2**: `328 + 64 + 98 = 490`
- **Problem 3**: `51 * 387 * 215 = 4,243,455`
- **Problem 4**: `64 + 23 + 314 = 401`

The grand total (sum of all answers) is: `33,210 + 490 + 4,243,455 + 401 = 4,277,556`

## Understanding the Format

Here's what I figured out:

1. **Problems are separated by empty columns** - If a column is all spaces from top to bottom, it's a separator
2. **Numbers are stacked vertically** - Each number in a problem appears in its own row
3. **The operator is at the bottom** - Either `+` for addition or `*` for multiplication
4. **Numbers can be right-aligned or variably positioned** - Don't assume they're all in the same position

## My Approach

### Step 1: Find Problem Boundaries

I scan through each column to identify which ones are completely empty (all spaces). These are the separators between problems.

### Step 2: Extract Each Problem

For each section between separators:

- Look at the bottom row to find the operator (`+` or `*`)
- Scan through the number rows and extract each number from that column range
- Numbers might be right-aligned or have different widths, so I grab the whole segment and strip whitespace

### Step 3: Calculate Results

For each problem:

- If it's addition (`+`): sum all the numbers
- If it's multiplication (`*`): multiply all the numbers together

### Step 4: Sum Everything

Add up all the individual problem results to get the grand total.

## The Algorithm

```python
def solve():
    # Read and normalize the input (pad all lines to same length)
    lines = [line.ljust(max_len) for line in lines]

    # Find separator columns (all spaces)
    separators = [col for col in range(max_len)
                  if is_all_spaces(lines, col)]

    # Extract problem ranges
    problem_ranges = extract_ranges(separators)

    # For each problem:
    for start_col, end_col in problem_ranges:
        # Get operator from last row
        operator = find_operator(lines[-1], start_col, end_col)

        # Extract all numbers in this range
        numbers = []
        for row in lines[:-1]:
            segment = row[start_col:end_col+1].strip()
            if segment.isdigit():
                numbers.append(int(segment))

        # Calculate based on operator
        result = sum(numbers) if operator == '+' else product(numbers)
        grand_total += result

    return grand_total
```

## Complexity

- **Time**: O(R × C) where R is the number of rows and C is the number of columns
- **Space**: O(C) for storing the lines

Not bad for trash compactor math!

## The Answer

After processing all the problems in the actual input:

**Answer: 4,076,006,202,939**

That's over 4 trillion! These cephalopods aren't messing around with their homework.

## Key Insights

1. **Spatial parsing is tricky** - Had to be careful about how numbers are positioned in each column
2. **Empty columns are crucial** - They're the only reliable way to separate problems
3. **Strip whitespace aggressively** - Numbers can be padded differently in different rows
4. **Don't assume uniform formatting** - Each row might position its number differently within the column range

Now let's see what Part 2 has in store... 🦑
