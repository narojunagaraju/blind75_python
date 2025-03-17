# TC O(R⋅C)
# SC O(min(R⋅C))

def num_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j)

    return count

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return

    grid[i][j] = '0'  # Mark the cell as visited

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        new_row = i + direction[0]
        new_col = j + direction[1]

        dfs(grid, new_row, new_col)

# Example usage
grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print(num_islands(grid))