# TC O(m*n)
# SC O(m+n)

def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])

    zero_rows = [False] * rows
    zero_cols = [False] * cols

    # Find positions of zero elements
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True

    # Set entire rows to zero
    for i in range(rows):
        if zero_rows[i]:
            for j in range(cols):
                matrix[i][j] = 0

    # Set entire columns to zero
    for j in range(cols):
        if zero_cols[j]:
            for i in range(rows):
                matrix[i][j] = 0


if __name__ == "__main__":
    input_matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    set_zeroes(input_matrix)

    for row in input_matrix:
        print(" ".join(map(str, row)))
