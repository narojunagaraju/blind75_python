# TC O(n^2)
# SC O(1)

def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

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
