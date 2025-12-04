def count_adjacent_rolls(grid, row, col):
    """
    Count the number of rolls (@) in the 8 adjacent positions.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Check all 8 adjacent positions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),           (0, 1),    # left, right
        (1, -1),  (1, 0),  (1, 1)     # bottom-left, bottom, bottom-right
    ]
    
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        # Check if the position is within bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == '@':
                count += 1
    
    return count

def find_accessible_rolls(grid):
    """
    Find all rolls that can be accessed by a forklift.
    A roll can be accessed if it has fewer than 4 adjacent rolls.
    """
    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0
    
    for row in range(rows):
        for col in range(cols):
            # Only check positions with rolls (@)
            if grid[row][col] == '@':
                adjacent_count = count_adjacent_rolls(grid, row, col)
                # Can access if fewer than 4 adjacent rolls
                if adjacent_count < 4:
                    accessible_count += 1
    
    return accessible_count

# Read input file
with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

# Convert to grid
grid = [list(line) for line in lines]

# Find accessible rolls
answer = find_accessible_rolls(grid)

print(f"Answer: {answer}")
