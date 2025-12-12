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
    """Get all unique orientations of a shape."""
    orientations = set()
    
    for flip in [False, True]:
        current = shape[:]
        if flip:
            current = [(-r, c) for r, c in current]
        
        for rotation in range(4):
            # Normalize
            if current:
                min_r = min(r for r, c in current)
                min_c = min(c for r, c in current)
                normalized = tuple(sorted([(r - min_r, c - min_c) for r, c in current]))
                orientations.add(normalized)
            
            # Rotate 90 degrees
            current = [(c, -r) for r, c in current]
    
    return list(orientations)



def solve_region(width, height, shapes, shape_counts):
    """Ultra-fast solver with aggressive pruning."""
    # Build list of presents to place
    presents = []
    for shape_id, count in enumerate(shape_counts):
        for _ in range(count):
            presents.append(shape_id)
    
    if not presents:
        return True
    
    # Sort by shape size (larger shapes first)
    presents.sort(key=lambda sid: len(shapes[sid]), reverse=True)
    
    # Calculate total cells needed
    total_cells_needed = sum(len(shapes[sid]) for sid in presents)
    if total_cells_needed > width * height:
        return False
    
    # Precompute all orientations and valid placements for each shape
    all_placements = {}
    for shape_id in set(presents):
        orientations = get_all_rotations_and_flips(shapes[shape_id])
        placements = []
        for orient in orientations:
            for r in range(height):
                for c in range(width):
                    # Check if orientation fits in bounds
                    valid = True
                    cells = []
                    for dr, dc in orient:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= height or nc < 0 or nc >= width:
                            valid = False
                            break
                        cells.append((nr, nc))
                    if valid:
                        placements.append(frozenset(cells))
        all_placements[shape_id] = placements
    
    # Use bitset for ultra-fast occupied tracking
    occupied = 0
    
    def cell_to_bit(r, c):
        return r * width + c
    
    def backtrack(present_idx, occupied_set):
        if present_idx == len(presents):
            return True
        
        shape_id = presents[present_idx]
        
        # Try each precomputed placement
        for placement in all_placements[shape_id]:
            # Quick check if any cell is occupied
            if any(cell in occupied_set for cell in placement):
                continue
            
            # Place the shape
            new_occupied = occupied_set | placement
            
            # Recurse
            if backtrack(present_idx + 1, new_occupied):
                return True
        
        return False
    
    return backtrack(0, frozenset())

def main():
    shapes, regions = parse_input('input.txt')
    
    print(f"Parsed {len(shapes)} shapes and {len(regions)} regions")
    
    solvable_count = 0
    for i, (width, height, counts) in enumerate(regions):
        print(f"Checking region {i+1}/{len(regions)}: {width}x{height}...", end=' ')
        if solve_region(width, height, shapes, counts):
            print("✓ Solvable")
            solvable_count += 1
        else:
            print("✗ Not solvable")
    
    print(f"\nTotal regions that can fit all presents: {solvable_count}")

if __name__ == "__main__":
    main()
