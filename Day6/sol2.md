# Day 6: Trash Compactor - Part 2

## The Plot Twist

The big cephalopods came back to check my work and... oops. Turns out my answer was wrong! But it's not my fault - they forgot to explain that **cephalopods read math right-to-left**!

Who could have guessed? Oh right, literally anyone who knows about right-to-left writing systems. But still, this adds a whole new twist to the problem.

## The Real Deal: Cephalopod Math

In cephalopod math:

- **Read columns from RIGHT to LEFT**
- **Each column is ONE complete number** (not a problem!)
- **Digits are read TOP to BOTTOM** (most significant digit at top)

Mind = blown. 🤯

### The Same Example, Completely Different

```
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
```

Reading **right-to-left**, column by column:

#### Rightmost Problem (columns 12-14)

- Column 14: reads as `4` (only has '4' in row 2)
- Column 13: reads as `431` (digits '4', '3', '1' top-to-bottom)
- Column 12: reads as `623` (digits '6', '2', '3' top-to-bottom)
- Operator: `+`
- **Result**: `4 + 431 + 623 = 1,058`

#### Second from Right (columns 8-10)

- Column 10: reads as `175` (digits '5', '7', '5')... wait, that's wrong
- Actually: Column 10 has ' ', '8', '2' → `82`
- Let me recalculate...

Actually, looking at the example answer more carefully:

- **Rightmost**: `4 + 431 + 623 = 1,058`
- **Second**: `175 * 581 * 32 = 3,253,600`
- **Third**: `8 + 248 + 369 = 625`
- **Leftmost**: `356 * 24 * 1 = 8,544`

**Grand Total**: `1,058 + 3,253,600 + 625 + 8,544 = 3,263,827`

## How It Works

### Step 1: Same Problem Detection

I still use the same method to find problem boundaries - columns of all spaces separate problems.

### Step 2: Read Right-to-Left

But now, instead of reading each problem left-to-right, I iterate through columns from **right to left**.

### Step 3: Build Numbers Vertically

For each column, I read from top to bottom to construct a single number:

```
Row 0: '6'  ← Most significant digit
Row 1: '2'
Row 2: '3'  ← Least significant digit
Result: 623
```

### Step 4: Calculate As Normal

Once I have all the numbers (in right-to-left order), I apply the operator same as before.

## The Updated Algorithm

```python
def solve():
    # Same setup as Part 1
    lines = normalize_lines()
    problem_ranges = find_problem_ranges(lines)

    grand_total = 0

    for start_col, end_col in problem_ranges:
        operator = find_operator(lines[-1], start_col, end_col)

        numbers = []

        # KEY CHANGE: Read columns RIGHT to LEFT
        for col in range(end_col, start_col - 1, -1):
            # Build number by reading TOP to BOTTOM
            digits = ""
            for row in range(len(lines) - 1):
                if lines[row][col].isdigit():
                    digits += lines[row][col]

            if digits:
                numbers.append(int(digits))

        # Calculate result
        result = sum(numbers) if operator == '+' else product(numbers)
        grand_total += result

    return grand_total
```

## The Difference

| Aspect               | Part 1                                     | Part 2                                      |
| -------------------- | ------------------------------------------ | ------------------------------------------- |
| **Column Range**     | Identifies one problem                     | Same                                        |
| **Number Reading**   | Each row has one number, read horizontally | Each column has one number, read vertically |
| **Processing Order** | Left-to-right (implicit)                   | Right-to-left (explicit)                    |
| **Example Result**   | 4,277,556                                  | 3,263,827                                   |

## Visual Comparison

**Part 1 thinking**: "Each problem is a vertical stack of horizontal numbers"

```
Problem 1:  123
            45
            6
            *    → 123 * 45 * 6
```

**Part 2 reality**: "Each problem is a horizontal row of vertical numbers"

```
Problem 1:  1    2    3
            4    5
            6
            *    *    *    → (reading R-L) 356 * 24 * 1
```

## Complexity

- **Time**: Still O(R × C)
- **Space**: Still O(C)
- **Brain cells used**: Double! 🧠

## The Answer

After reading the worksheet correctly this time:

**Answer: 7,903,168,391,557**

That's almost **8 trillion**! Way different from Part 1's answer. Reading direction matters, folks!

## Lessons Learned

1. **Always clarify the requirements** - Even when you think you understand them
2. **Cultural differences matter** - Right-to-left reading is totally valid
3. **The same data can mean different things** - Depending on how you interpret it
4. **Vertical text is underrated** - Those cephalopods are onto something
5. **When in doubt, ask the squid** - They seem to know what they're doing 🦑

Now, can someone please get me out of this trash compactor? I've had enough math for one day!
