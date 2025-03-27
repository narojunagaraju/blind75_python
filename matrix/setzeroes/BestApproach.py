# TC O(m*n)
# SC O(1)

def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])

    first_row_zero = False
    first_col_zero = False

    # Check if the first row should be zeroed
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Check if the first column should be zeroed
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    # Mark rows and columns to be zeroed using the first row and column
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set entire rows to zero except for the first row
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(1, cols):
                matrix[i][j] = 0

    # Set entire columns to zero except for the first column
    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(1, rows):
                matrix[i][j] = 0

    # Set the first row to zero if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Set the first column to zero if needed
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


if __name__ == "__main__":
    input_matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    set_zeroes(input_matrix)

    for row in input_matrix:
        print(" ".join(map(str, row)))
