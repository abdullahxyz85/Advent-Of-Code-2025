def parse_input(input_text):
    """
    Parse the input into fresh ranges and available ingredient IDs.
    """
    lines = input_text.strip().split('\n')
    
    # Find the blank line that separates ranges from IDs
    blank_index = lines.index('')
    
    # Parse fresh ranges
    ranges = []
    for line in lines[:blank_index]:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    
    # Parse available ingredient IDs
    ingredient_ids = []
    for line in lines[blank_index + 1:]:
        if line.strip():
            ingredient_ids.append(int(line.strip()))
    
    return ranges, ingredient_ids

def is_fresh(ingredient_id, ranges):
    """
    Check if an ingredient ID falls within any fresh range.
    """
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def count_fresh_ingredients(input_text):
    """
    Count how many available ingredient IDs are fresh.
    """
    ranges, ingredient_ids = parse_input(input_text)
    
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        if is_fresh(ingredient_id, ranges):
            fresh_count += 1
    
    return fresh_count

# Read input file
with open('input.txt', 'r') as f:
    input_data = f.read()

# Solve the puzzle
answer = count_fresh_ingredients(input_data)

print(f"Answer: {answer}")
