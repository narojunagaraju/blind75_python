# TC O(n^2)
# SC O(1)

def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_matrix(matrix)

    print("Printing the rotated matrix")
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
