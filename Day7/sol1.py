def solve():
    with open('input.txt', 'r') as f:
        grid = [line.rstrip('\n') for line in f.readlines()]
    
    # Find the starting position 'S'
    start_row, start_col = None, None
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == 'S':
                start_row, start_col = r, c
                break
        if start_row is not None:
            break
    
    # Track beams and count splits
    # All beams only move downward
    # When a beam hits a splitter, it stops and creates two new beams
    # immediately to the left and right of the splitter
    beams = [(start_row, start_col)]
    visited = set()  # Track (row, col) to avoid infinite loops
    split_count = 0
    
    while beams:
        row, col = beams.pop(0)
        
        # Check if we've already processed this beam position
        if (row, col) in visited:
            continue
        visited.add((row, col))
        
        # Beam moves downward one step
        next_row, next_col = row + 1, col
        
        # Check if beam exits the manifold
        if next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]):
            continue
        
        # Check what's at the next position
        next_char = grid[next_row][next_col] if next_col < len(grid[next_row]) else '.'
        
        if next_char == '^':
            # Beam hits a splitter - it stops and creates two new beams
            # New beams start immediately left and right of the splitter
            split_count += 1
            if next_col - 1 >= 0:
                beams.append((next_row, next_col - 1))
            if next_col + 1 < len(grid[next_row]):
                beams.append((next_row, next_col + 1))
        elif next_char == '.':
            # Empty space - beam continues downward
            beams.append((next_row, next_col))
    
    return split_count

answer = solve()
print(f"Answer: {answer}")
