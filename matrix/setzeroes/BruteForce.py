# TC O(m*n)
# SC O(m+n)

def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    # Find the positions of zero elements
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set entire rows to zero
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0

    # Set entire columns to zero
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0


if __name__ == "__main__":
    input_matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    set_zeroes(input_matrix)

    for row in input_matrix:
        print(" ".join(map(str, row)))
