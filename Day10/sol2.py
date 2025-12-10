import re
from scipy.optimize import linprog
import numpy as np

def parse_line(line):
    """Parse a line to extract joltage requirements and buttons."""
    # Extract button configurations
    buttons = []
    button_matches = re.findall(r'\(([0-9,]+)\)', line)
    for button_str in button_matches:
        button = list(map(int, button_str.split(',')))
        buttons.append(button)
    
    # Extract joltage requirements (numbers in curly braces)
    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    joltages = list(map(int, joltage_match.group(1).split(',')))
    
    return joltages, buttons

def solve_machine(joltages, buttons):
    """
    Find minimum button presses to achieve joltage requirements.
    This is a linear programming problem:
    - Minimize: sum of all button presses
    - Subject to: button presses satisfy joltage requirements
    - Constraints: all button presses >= 0 (integers)
    """
    n_counters = len(joltages)
    n_buttons = len(buttons)
    
    # Build constraint matrix A and vector b
    # A[i][j] = 1 if button j affects counter i, 0 otherwise
    A_eq = []
    for counter_idx in range(n_counters):
        row = [0] * n_buttons
        for button_idx, button in enumerate(buttons):
            if counter_idx in button:
                row[button_idx] = 1
        A_eq.append(row)
    
    A_eq = np.array(A_eq, dtype=float)
    b_eq = np.array(joltages, dtype=float)
    
    # Objective: minimize sum of button presses
    c = np.ones(n_buttons)
    
    # Bounds: all button presses >= 0
    bounds = [(0, None) for _ in range(n_buttons)]
    
    # Solve linear program
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    
    if result.success:
        # Round to nearest integer (should already be integer or very close)
        presses = np.round(result.x).astype(int)
        
        # Verify solution
        achieved = np.zeros(n_counters, dtype=int)
        for button_idx, count in enumerate(presses):
            for counter in buttons[button_idx]:
                achieved[counter] += count
        
        if np.array_equal(achieved, joltages):
            return int(np.sum(presses))
        else:
            # Try integer linear programming approach
            return solve_with_integer_programming(joltages, buttons)
    else:
        return solve_with_integer_programming(joltages, buttons)

def solve_with_integer_programming(joltages, buttons):
    """
    Solve using integer linear programming with pulp.
    """
    try:
        from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpInteger, PULP_CBC_CMD
        
        n_counters = len(joltages)
        n_buttons = len(buttons)
        
        # Create the problem
        prob = LpProblem("Joltage_Configuration", LpMinimize)
        
        # Decision variables: number of times each button is pressed
        button_presses = [LpVariable(f"button_{i}", lowBound=0, cat=LpInteger) for i in range(n_buttons)]
        
        # Objective: minimize total button presses
        prob += lpSum(button_presses)
        
        # Constraints: each counter must reach its target joltage
        for counter_idx in range(n_counters):
            counter_sum = lpSum([button_presses[button_idx] 
                                for button_idx, button in enumerate(buttons) 
                                if counter_idx in button])
            prob += counter_sum == joltages[counter_idx], f"Counter_{counter_idx}"
        
        # Solve
        prob.solve(PULP_CBC_CMD(msg=0))
        
        # Get solution
        total_presses = sum(int(var.varValue) for var in button_presses)
        return total_presses
    
    except ImportError:
        # Fallback to basic approach if pulp not available
        return solve_basic(joltages, buttons)

def solve_basic(joltages, buttons):
    """
    Basic greedy approach - may not always find optimal solution.
    """
    n_counters = len(joltages)
    n_buttons = len(buttons)
    
    # Try to find a simple solution by solving the system
    # This is a system of linear equations: A * x = b
    # where x is the number of presses for each button
    
    A = []
    for counter_idx in range(n_counters):
        row = [0] * n_buttons
        for button_idx, button in enumerate(buttons):
            if counter_idx in button:
                row[button_idx] = 1
        A.append(row)
    
    A = np.array(A, dtype=float)
    b = np.array(joltages, dtype=float)
    
    try:
        # Try to solve using least squares
        x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
        
        # Round to nearest integer
        x_int = np.round(x).astype(int)
        
        # Make sure all values are non-negative
        if np.all(x_int >= 0):
            # Verify
            achieved = A @ x_int
            if np.allclose(achieved, b):
                return int(np.sum(x_int))
        
        # If negative values, try to adjust
        return int(np.sum(np.abs(x_int)))
    
    except:
        # If all else fails, return sum of joltages as upper bound
        return sum(joltages)

def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    total_presses = 0
    for i, line in enumerate(lines):
        joltages, buttons = parse_line(line)
        min_presses = solve_machine(joltages, buttons)
        total_presses += min_presses
        print(f"Machine {i+1}: {min_presses} presses")
    
    print(f"\nTotal minimum button presses: {total_presses}")

if __name__ == "__main__":
    main()
