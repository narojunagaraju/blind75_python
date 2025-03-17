# TC O(R⋅C)
# SC O(min(R⋅C))

from collections import deque


def bfs(grid, i, j):
    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    queue.append((i, j))
    grid[i][j] = '0'

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current = queue.popleft()

        for direction in directions:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]

            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '1':
                grid[new_row][new_col] = '0'
                queue.append((new_row, new_col))


def num_islands(grid) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                bfs(grid, i, j)
                count += 1

    return count


grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print(num_islands(grid))
