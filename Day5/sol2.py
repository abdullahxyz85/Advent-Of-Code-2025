def parse_ranges(input_text):
    """
    Parse the input to extract only the fresh ranges.
    """
    lines = input_text.strip().split('\n')
    
    # Find the blank line that separates ranges from IDs
    blank_index = lines.index('')
    
    # Parse fresh ranges
    ranges = []
    for line in lines[:blank_index]:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    
    return ranges

def merge_overlapping_ranges(ranges):
    """
    Merge overlapping ranges to avoid double-counting IDs.
    """
    if not ranges:
        return []
    
    # Sort ranges by start position
    sorted_ranges = sorted(ranges)
    
    merged = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        # Check if current range overlaps or is adjacent to the last merged range
        if current_start <= last_end + 1:
            # Merge by extending the end if needed
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as new range
            merged.append((current_start, current_end))
    
    return merged

def count_fresh_ids(input_text):
    """
    Count all ingredient IDs that are considered fresh.
    """
    ranges = parse_ranges(input_text)
    
    # Merge overlapping ranges to get the actual count
    merged_ranges = merge_overlapping_ranges(ranges)
    
    # Count total IDs in all merged ranges
    total_fresh = 0
    for start, end in merged_ranges:
        # Range is inclusive, so add 1
        total_fresh += (end - start + 1)
    
    return total_fresh

# Read input file
with open('input.txt', 'r') as f:
    input_data = f.read()

# Solve the puzzle
answer = count_fresh_ids(input_data)

print(f"Answer: {answer}")
