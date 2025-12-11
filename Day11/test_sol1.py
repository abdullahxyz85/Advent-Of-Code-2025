def parse_input(filename):
    """Parse the input file and build a graph."""
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(': ')
            if len(parts) != 2:
                continue
            
            device = parts[0]
            outputs = parts[1].split()
            graph[device] = outputs
    
    return graph

def count_paths(graph, start, end, visited=None):
    """Count all paths from start to end using DFS."""
    if visited is None:
        visited = set()
    
    # If we reached the end, we found a path
    if start == end:
        return 1
    
    # If this node has no outputs, no path exists
    if start not in graph:
        return 0
    
    # Mark current node as visited to avoid cycles
    visited.add(start)
    
    total_paths = 0
    # Explore all neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            total_paths += count_paths(graph, neighbor, end, visited)
    
    # Backtrack: remove current node from visited set
    visited.remove(start)
    
    return total_paths

def main():
    # Test with example
    print("Testing with example:")
    graph = parse_input('test_input.txt')
    num_paths = count_paths(graph, "you", "out")
    print(f"Example: {num_paths} paths (expected: 5)")
    print()
    
    # Solve actual puzzle
    print("Solving actual puzzle:")
    graph = parse_input('input.txt')
    num_paths = count_paths(graph, "you", "out")
    print(f"Number of different paths from 'you' to 'out': {num_paths}")

if __name__ == "__main__":
    main()
