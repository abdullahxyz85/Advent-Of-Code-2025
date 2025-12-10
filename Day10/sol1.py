import re
from itertools import combinations

def parse_line(line):
    """Parse a line to extract target state and buttons."""
    # Extract indicator lights pattern
    lights_match = re.search(r'\[([.#]+)\]', line)
    target = [1 if c == '#' else 0 for c in lights_match.group(1)]
    
    # Extract button configurations
    buttons = []
    button_matches = re.findall(r'\(([0-9,]+)\)', line)
    for button_str in button_matches:
        button = set(map(int, button_str.split(',')))
        buttons.append(button)
    
    return target, buttons

def solve_machine(target, buttons):
    """
    Find minimum button presses to achieve target configuration.
    Uses brute force with optimization for small cases.
    """
    n_lights = len(target)
    n_buttons = len(buttons)
    
    # Try all possible combinations starting from smallest
    for total_presses in range(n_buttons + 1):
        # Try all combinations of buttons we could press
        for num_buttons in range(min(total_presses + 1, n_buttons + 1)):
            for button_combo in combinations(range(n_buttons), num_buttons):
                # Check if this combination works (each button pressed once)
                if len(button_combo) != total_presses:
                    if total_presses > n_buttons:
                        continue
                    # Need to press some buttons multiple times
                    # For now, only handle case where each selected button is pressed once
                    if len(button_combo) != total_presses:
                        continue
                
                # Simulate pressing these buttons
                state = [0] * n_lights
                for button_idx in button_combo:
                    for light in buttons[button_idx]:
                        state[light] = 1 - state[light]  # Toggle
                
                if state == target:
                    return total_presses
    
    # If simple approach doesn't work, use Gaussian elimination
    return solve_with_gaussian(target, buttons)

def solve_with_gaussian(target, buttons):
    """
    Solve using Gaussian elimination over GF(2).
    Returns minimum number of button presses (sum of solution vector).
    """
    n_lights = len(target)
    n_buttons = len(buttons)
    
    # Build augmented matrix: each row is an equation for one light
    # Columns are: [button0, button1, ..., buttonN-1, target]
    matrix = []
    for light_idx in range(n_lights):
        row = [0] * (n_buttons + 1)
        for button_idx, button in enumerate(buttons):
            if light_idx in button:
                row[button_idx] = 1
        row[n_buttons] = target[light_idx]
        matrix.append(row)
    
    # Gaussian elimination (row reduction) over GF(2)
    pivot_row = 0
    for col in range(n_buttons):
        # Find pivot
        found_pivot = False
        for row in range(pivot_row, n_lights):
            if matrix[row][col] == 1:
                # Swap rows
                matrix[pivot_row], matrix[row] = matrix[row], matrix[pivot_row]
                found_pivot = True
                break
        
        if not found_pivot:
            continue
        
        # Eliminate column in other rows
        for row in range(n_lights):
            if row != pivot_row and matrix[row][col] == 1:
                for c in range(n_buttons + 1):
                    matrix[row][c] = (matrix[row][c] + matrix[pivot_row][c]) % 2
        
        pivot_row += 1
    
    # Back substitution to find solution
    solution = [0] * n_buttons
    
    for row in range(min(pivot_row, n_lights) - 1, -1, -1):
        # Find leading 1
        leading_col = -1
        for col in range(n_buttons):
            if matrix[row][col] == 1:
                leading_col = col
                break
        
        if leading_col == -1:
            # Check if inconsistent
            if matrix[row][n_buttons] == 1:
                # No solution exists - shouldn't happen for valid input
                return float('inf')
            continue
        
        # Solve for this variable
        val = matrix[row][n_buttons]
        for col in range(leading_col + 1, n_buttons):
            val = (val + matrix[row][col] * solution[col]) % 2
        solution[leading_col] = val
    
    return sum(solution)

def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    total_presses = 0
    for line in lines:
        target, buttons = parse_line(line)
        min_presses = solve_machine(target, buttons)
        total_presses += min_presses
    
    print(f"Total minimum button presses: {total_presses}")

if __name__ == "__main__":
    main()
