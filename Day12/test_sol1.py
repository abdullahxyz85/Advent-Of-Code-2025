def parse_input(filename):
    """Parse shapes and regions from input file."""
    with open(filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    
    shapes = {}
    regions = []
    
    i = 0
    # Parse shapes
    while i < len(lines):
        line = lines[i]
        if ':' in line and not 'x' in line:
            shape_id = int(line.rstrip(':'))
            shape_lines = []
            i += 1
            while i < len(lines) and lines[i] and 'x' not in lines[i] and ':' not in lines[i]:
                shape_lines.append(lines[i])
                i += 1
            shapes[shape_id] = parse_shape(shape_lines)
        elif 'x' in line:
            # Parse region
            parts = line.split(': ')
            dims = parts[0].split('x')
            width, height = int(dims[0]), int(dims[1])
            counts = list(map(int, parts[1].split()))
            regions.append((width, height, counts))
            i += 1
        else:
            i += 1
    
    return shapes, regions

def parse_shape(lines):
    """Convert shape lines to list of (row, col) coordinates."""
    coords = []
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == '#':
                coords.append((r, c))
    return coords

def get_all_rotations_and_flips(shape):
    """Get all 8 possible orientations of a shape."""
    orientations = []
    
    # Original
    orientations.append(shape)
    
    # Rotate 90, 180, 270
    for _ in range(3):
        shape = [(c, -r) for r, c in shape]
        orientations.append(shape)
    
    # Flip horizontally
    shape = [(-r, c) for r, c in shape]
    orientations.append(shape)
    
    # Rotate flipped version
    for _ in range(3):
        shape = [(c, -r) for r, c in shape]
        orientations.append(shape)
    
    # Normalize all orientations
    normalized = []
    for orient in orientations:
        min_r = min(r for r, c in orient)
        min_c = min(c for r, c in orient)
        normalized_orient = tuple(sorted([(r - min_r, c - min_c) for r, c in orient]))
        if normalized_orient not in normalized:
            normalized.append(normalized_orient)
    
    return normalized

def can_place_shape(grid, shape, start_r, start_c, width, height):
    """Check if shape can be placed at given position."""
    for dr, dc in shape:
        r, c = start_r + dr, start_c + dc
        if r < 0 or r >= height or c < 0 or c >= width:
            return False
        if grid[r][c]:
            return False
    return True

def place_shape(grid, shape, start_r, start_c):
    """Place shape on grid."""
    for dr, dc in shape:
        r, c = start_r + dr, start_c + dc
        grid[r][c] = True

def remove_shape(grid, shape, start_r, start_c):
    """Remove shape from grid."""
    for dr, dc in shape:
        r, c = start_r + dr, start_c + dc
        grid[r][c] = False

def solve_region(width, height, shapes, shape_counts):
    """Try to fit all required shapes into the region using backtracking."""
    grid = [[False] * width for _ in range(height)]
    
    # Build list of presents to place
    presents = []
    for shape_id, count in enumerate(shape_counts):
        for _ in range(count):
            presents.append(shape_id)
    
    # Precompute all orientations for each shape
    all_orientations = {}
    for shape_id in shapes:
        all_orientations[shape_id] = get_all_rotations_and_flips(shapes[shape_id])
    
    def backtrack(present_idx):
        if present_idx == len(presents):
            return True
        
        shape_id = presents[present_idx]
        
        # Try all orientations
        for orientation in all_orientations[shape_id]:
            # Try all positions
            for r in range(height):
                for c in range(width):
                    if can_place_shape(grid, orientation, r, c, width, height):
                        place_shape(grid, orientation, r, c)
                        if backtrack(present_idx + 1):
                            return True
                        remove_shape(grid, orientation, r, c)
        
        return False
    
    return backtrack(0)

def main():
    # Test with example
    print("Testing with example:")
    shapes, regions = parse_input('test_input.txt')
    print(f"Parsed {len(shapes)} shapes and {len(regions)} regions")
    
    solvable_count = 0
    for i, (width, height, counts) in enumerate(regions):
        print(f"Region {i+1}: {width}x{height} with {sum(counts)} presents...", end=' ')
        if solve_region(width, height, shapes, counts):
            print("✓ Solvable")
            solvable_count += 1
        else:
            print("✗ Not solvable")
    
    print(f"Example result: {solvable_count} regions (expected: 2)")
    print()
    
    # Solve actual puzzle
    print("Solving actual puzzle:")
    shapes, regions = parse_input('input.txt')
    print(f"Parsed {len(shapes)} shapes and {len(regions)} regions")
    
    solvable_count = 0
    for i, (width, height, counts) in enumerate(regions):
        print(f"Checking region {i+1}/{len(regions)}: {width}x{height}...", end=' ', flush=True)
        if solve_region(width, height, shapes, counts):
            print("✓")
            solvable_count += 1
        else:
            print("✗")
    
    print(f"\nTotal regions that can fit all presents: {solvable_count}")

if __name__ == "__main__":
    main()
