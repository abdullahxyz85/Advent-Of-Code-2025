def count_adjacent_rolls(grid, row, col):
    """
    Count the number of rolls (@) in the 8 adjacent positions.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == '@':
                count += 1
    
    return count

def find_accessible_rolls(grid):
    """
    Find all rolls that can currently be accessed by a forklift.
    Returns a list of (row, col) positions.
    """
    rows = len(grid)
    cols = len(grid[0])
    accessible = []
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                adjacent_count = count_adjacent_rolls(grid, row, col)
                if adjacent_count < 4:
                    accessible.append((row, col))
    
    return accessible

def remove_all_possible_rolls(grid):
    """
    Repeatedly remove accessible rolls until no more can be removed.
    Returns the total number of rolls removed.
    """
    # Make a copy of the grid to modify
    grid = [row[:] for row in grid]
    total_removed = 0
    
    while True:
        # Find all currently accessible rolls
        accessible = find_accessible_rolls(grid)
        
        if not accessible:
            # No more rolls can be removed
            break
        
        # Remove all accessible rolls
        for row, col in accessible:
            grid[row][col] = '.'
        
        total_removed += len(accessible)
    
    return total_removed

# Read input file
with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

# Convert to grid
grid = [list(line) for line in lines]

# Remove all possible rolls
answer = remove_all_possible_rolls(grid)

print(f"Answer: {answer}")
