def is_invalid_id(num):
    """
    Check if a number is invalid (made of a sequence repeated twice).
    Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
    """
    s = str(num)
    length = len(s)
    
    # Must be even length to be split into two equal parts
    if length % 2 != 0:
        return False
    
    # Split in half and check if both halves are identical
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    # First half shouldn't have leading zeros (unless it's just "0")
    if first_half[0] == '0' and len(first_half) > 1:
        return False
    
    return first_half == second_half

def solve_puzzle(input_text):
    """
    Parse ranges and find all invalid IDs within them.
    """
    ranges = input_text.strip().split(',')
    
    total_sum = 0
    
    for range_str in ranges:
        range_str = range_str.strip()
        if not range_str:
            continue
            
        start, end = map(int, range_str.split('-'))
        
        # Check each number in the range
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total_sum += num
    
    return total_sum

# Read input file
with open('input.txt', 'r') as f:
    input_data = f.read()

# Solve the puzzle
answer = solve_puzzle(input_data)

print(f"Answer: {answer}")
