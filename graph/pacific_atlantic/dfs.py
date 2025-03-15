# TC O(R⋅C)
# SC O(R⋅C)

def pacific_atlantic(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    pacific_reachable = [[False] * cols for _ in range(rows)]
    atlantic_reachable = [[False] * cols for _ in range(rows)]

    for i in range(rows):
        dfs(matrix, pacific_reachable, i, 0)
        dfs(matrix, atlantic_reachable, i, cols - 1)

    for j in range(cols):
        dfs(matrix, pacific_reachable, 0, j)
        dfs(matrix, atlantic_reachable, rows - 1, j)

    result = []
    for i in range(rows):
        for j in range(cols):
            if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                result.append([i, j])

    return result

def dfs(matrix, reachable, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    reachable[row][col] = True

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        if (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and
            matrix[new_row][new_col] >= matrix[row][col] and not reachable[new_row][new_col]):
            dfs(matrix, reachable, new_row, new_col)

# Example Usage
matrix = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
print(pacific_atlantic(matrix))
