def dfs(grid, r, c, visited):
    if r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 0

    position = (r, c)
    if position in visited:
        return 0

    visited.add(position)

    if grid[r][c] == "^":
        return 1 + dfs(grid, r + 1, c - 1, visited) + dfs(grid, r + 1, c + 1, visited)
    else:
        return dfs(grid, r + 1, c, visited)


with open("input.txt") as f:
    grid = [line.rstrip("\n") for line in f.readlines()]

print(dfs(grid, 0, grid[0].index('S'), set()))
