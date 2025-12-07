DIRECTION_OFFSETS = []

for dx in (-1, 0, 1):
    for dy in (-1, 0, 1):
        if dx == 0 and dy == 0:
            continue
        DIRECTION_OFFSETS.append((dx, dy))

with open("input.txt") as f:
    grid = [list(line.strip()) for line in f if line.strip()]

total = 0

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell != "@":
            continue

        count = 0

        for offset in DIRECTION_OFFSETS:
            adj_row, adj_col = r + offset[0], c + offset[1]
            if 0 <= adj_row < len(grid) and 0 <= adj_col < len(row):
                count += grid[adj_row][adj_col] == "@"

        if count < 4:
            total += 1

print(total)
