def solve():
    with open('input.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    # Ensure all lines have the same length by padding with spaces
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]
    
    # Identify problem boundaries by finding columns that are ALL spaces
    def is_separator_column(lines, col):
        """Check if a column is all spaces (separator)"""
        for line in lines:
            if col < len(line) and line[col] != ' ':
                return False
        return True
    
    # Find problem boundaries
    separators = []
    for col in range(max_len):
        if is_separator_column(lines, col):
            separators.append(col)
    
    # Extract problems between separators
    problem_ranges = []
    start = 0
    for sep in separators:
        if sep > start:
            problem_ranges.append((start, sep - 1))
        start = sep + 1
    
    if start < max_len:
        problem_ranges.append((start, max_len - 1))
    
    # For each problem range, extract numbers and operator
    grand_total = 0
    for start_col, end_col in problem_ranges:
        # Get operator from last line
        operator = None
        for col in range(start_col, end_col + 1):
            if lines[-1][col] in ['+', '*']:
                operator = lines[-1][col]
                break
        
        if operator is None:
            continue
        
        # Extract all numbers from this range
        numbers = []
        for row in lines[:-1]:  # All rows except operator row
            segment = row[start_col:end_col + 1].strip()
            if segment and segment.isdigit():
                numbers.append(int(segment))
        
        # Calculate result
        if operator == '+':
            result = sum(numbers)
        else:
            result = 1
            for num in numbers:
                result *= num
        
        grand_total += result
    
    return grand_total

answer = solve()
print(f"Answer: {answer}")
