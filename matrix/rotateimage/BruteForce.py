# TC O(n^2)
# SC O(n^2)

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

def rotate_matrix(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = result[i][j]

if __name__ == "__main__":
    main()
