# TC O(R⋅C)
# SC O(R⋅C)

from collections import deque


def pacific_atlantic(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    pacific_reachable = [[False] * cols for _ in range(rows)]
    atlantic_reachable = [[False] * cols for _ in range(rows)]

    pacific_queue = deque([(i, 0) for i in range(rows)] + [(0, j) for j in range(cols)])
    atlantic_queue = deque([(i, cols - 1) for i in range(rows)] + [(rows - 1, j) for j in range(cols)])

    for i in range(rows):
        pacific_reachable[i][0] = True
        atlantic_reachable[i][cols - 1] = True

    for j in range(cols):
        pacific_reachable[0][j] = True
        atlantic_reachable[rows - 1][j] = True

    bfs(matrix, pacific_queue, pacific_reachable)
    bfs(matrix, atlantic_queue, atlantic_reachable)

    result = []
    for i in range(rows):
        for j in range(cols):
            if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                result.append([i, j])

    return result

def bfs(matrix, queue, reachable):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and
                matrix[new_row][new_col] >= matrix[row][col] and not reachable[new_row][new_col]):
                reachable[new_row][new_col] = True
                queue.append((new_row, new_col))


matrix = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
print(pacific_atlantic(matrix))

