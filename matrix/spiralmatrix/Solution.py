# TC : O(m * n)
# SC: O(1)

def spiral_order(matrix):
    result = []

    if not matrix or not matrix[0]:
        return result

    rows, cols = len(matrix), len(matrix[0])
    left, right, top, bottom = 0, cols - 1, 0, rows - 1

    while left <= right and top <= bottom:
        # Traverse top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    res = spiral_order(matrix)
    print(res)
