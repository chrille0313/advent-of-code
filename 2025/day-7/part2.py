def dp(grid, r, c, memo):
    if r == len(grid):
        return 1
    elif c < 0 or c >= len(grid[0]):
        return 0

    state = (r, c)
    if state in memo:
        return memo[(r, c)]

    if grid[r][c] == "^":
        memo[state] = dp(grid, r + 1, c - 1, memo) + dp(grid, r + 1, c + 1, memo)
    else:
        memo[state] = dp(grid, r + 1, c, memo)

    return memo[state]


with open("input.txt") as f:
    grid = [line.rstrip("\n") for line in f.readlines()]

print(dp(grid, 0, grid[0].index('S'), {}))
