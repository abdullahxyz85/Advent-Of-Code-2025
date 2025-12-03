def find_max_joltage_part2(bank, num_batteries=12):
    """
    Find the maximum joltage by selecting exactly num_batteries batteries.
    Strategy: Greedily select the largest digits while maintaining position order.
    
    This is similar to finding the largest subsequence of length k.
    """
    digits = str(bank).strip()
    n = len(digits)
    
    # We need to select num_batteries digits from n total digits
    # We must drop (n - num_batteries) digits
    to_drop = n - num_batteries
    
    if to_drop < 0:
        # Not enough digits in the bank
        return int(digits)
    
    if to_drop == 0:
        # Use all digits
        return int(digits)
    
    # Use a greedy approach with a stack
    # We want to keep the largest digits while maintaining order
    stack = []
    
    for i, digit in enumerate(digits):
        # While we can still drop digits and the current digit is larger
        # than the last digit in our stack, remove from stack
        while stack and to_drop > 0 and stack[-1] < digit:
            stack.pop()
            to_drop -= 1
        
        stack.append(digit)
    
    # If we still need to drop more digits, drop from the end
    while to_drop > 0:
        stack.pop()
        to_drop -= 1
    
    # Convert the selected digits back to integer
    result = int(''.join(stack))
    return result

def solve_puzzle_part2(input_text):
    """
    Calculate the total output joltage by finding max joltage from each bank.
    Now we select 12 batteries per bank.
    """
    banks = input_text.strip().split('\n')
    total_joltage = 0
    
    for bank in banks:
        if bank.strip():
            max_jolt = find_max_joltage_part2(bank.strip(), 12)
            total_joltage += max_jolt
    
    return total_joltage

# Read input file
with open('input.txt', 'r') as f:
    input_data = f.read()

# Solve the puzzle
answer = solve_puzzle_part2(input_data)

print(f"Answer: {answer}")
