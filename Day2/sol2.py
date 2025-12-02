def is_invalid_id_part2(num):
    """
    Check if a number is invalid (made of a sequence repeated at least twice).
    Examples: 
    - 12341234 (1234 two times)
    - 123123123 (123 three times)
    - 1212121212 (12 five times)
    - 1111111 (1 seven times)
    """
    s = str(num)
    length = len(s)
    
    # Try all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the string length is divisible by pattern length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            
            # Check if pattern has leading zeros (invalid unless it's just "0")
            if pattern[0] == '0' and len(pattern) > 1:
                continue
            
            # Check if the entire string is this pattern repeated
            repetitions = length // pattern_len
            if pattern * repetitions == s and repetitions >= 2:
                return True
    
    return False

def solve_puzzle_part2(input_text):
    """
    Parse ranges and find all invalid IDs within them (Part 2 rules).
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
            if is_invalid_id_part2(num):
                total_sum += num
    
    return total_sum

# Read input file
with open('input.txt', 'r') as f:
    input_data = f.read()

# Solve the puzzle
answer = solve_puzzle_part2(input_data)

print(f"Answer: {answer}")
