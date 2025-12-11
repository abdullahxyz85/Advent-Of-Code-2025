from functools import lru_cache

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

def count_paths_optimized(graph, start, end, required_nodes):
    """Count paths using dynamic programming with memoization."""
    required_set = frozenset(required_nodes)
    
    # Memoization: (current_node, visited_required_as_frozenset) -> count
    memo = {}
    
    def dfs(node, visited_path, visited_required):
        # If we reached the end
        if node == end:
            return 1 if visited_required == required_set else 0
        
        # Create memo key
        key = (node, visited_required)
        if key in memo:
            return memo[key]
        
        # If no outputs, return 0
        if node not in graph:
            memo[key] = 0
            return 0
        
        # Track if this node is required
        new_visited_required = visited_required
        if node in required_set:
            new_visited_required = visited_required | frozenset([node])
        
        total = 0
        for neighbor in graph[node]:
            if neighbor not in visited_path:
                new_visited = visited_path | frozenset([neighbor])
                total += dfs(neighbor, new_visited, new_visited_required)
        
        memo[key] = total
        return total
    
    return dfs(start, frozenset([start]), frozenset([start]) if start in required_set else frozenset())

def main():
    # Test with example
    print("Testing with example:")
    test_graph = {
        'svr': ['aaa', 'bbb'],
        'aaa': ['fft'],
        'fft': ['ccc'],
        'bbb': ['tty'],
        'tty': ['ccc'],
        'ccc': ['ddd', 'eee'],
        'ddd': ['hub'],
        'hub': ['fff'],
        'eee': ['dac'],
        'dac': ['fff'],
        'fff': ['ggg', 'hhh'],
        'ggg': ['out'],
        'hhh': ['out']
    }
    
    required = {'dac', 'fft'}
    count = count_paths_optimized(test_graph, 'svr', 'out', required)
    print(f"Example: {count} paths visit both 'dac' and 'fft' (expected: 2)")
    print()
    
    # Solve actual puzzle
    print("Solving actual puzzle:")
    graph = parse_input('input.txt')
    count = count_paths_optimized(graph, 'svr', 'out', required)
    print(f"Number of paths from 'svr' to 'out' that visit both 'dac' and 'fft': {count}")

if __name__ == "__main__":
    main()
