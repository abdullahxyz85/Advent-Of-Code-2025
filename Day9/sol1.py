# Read input
with open('input.txt', 'r') as f:
    lines = f.readlines()

red_tiles = []
for line in lines:
    x, y = map(int, line.strip().split(','))
    red_tiles.append((x, y))

# For each pair of red tiles, calculate the rectangle area (inclusive)
max_area = 0
best_pair = None

for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        
        # Calculate rectangle area (inclusive of endpoints)
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height
        
        if area > max_area:
            max_area = area
            best_pair = (red_tiles[i], red_tiles[j])

print(f"Maximum area: {max_area}")
print(f"Best pair: {best_pair}")
