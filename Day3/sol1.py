def find_max_joltage(bank):
    """
    Find the maximum joltage from a battery bank by selecting two batteries.
    We need to find the two digits that form the largest possible number.
    """
    # Convert to string to work with individual digits
    digits = str(bank)
    max_joltage = 0
    
    # Try all pairs of positions (i, j) where i < j
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            # Form the number using digits at positions i and j
            joltage = int(digits[i] + digits[j])
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

def solve_puzzle(input_text):
    """
    Calculate the total output joltage by finding max joltage from each bank.
    """
    banks = input_text.strip().split('\n')
    total_joltage = 0
    
    for bank in banks:
        if bank.strip():  # Skip empty lines
            max_jolt = find_max_joltage(bank.strip())
            total_joltage += max_jolt
    
    return total_joltage

# Read input file
with open('input.txt', 'r') as f:
    input_data = f.read()

# Solve the puzzle
answer = solve_puzzle(input_data)

print(f"Answer: {answer}")
