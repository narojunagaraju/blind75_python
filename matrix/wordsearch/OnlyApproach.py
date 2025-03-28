# TC O(N * M * 4^L)
# SC O(L)

def exist(board, word):
    rows, cols = len(board), len(board[0])

    def search_word(i, j, index):
        if index == len(word):
            return True

        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[index]:
            return False

        # Mark the current cell as visited
        temp, board[i][j] = board[i][j], '.'

        # Explore neighbors
        found = (
            search_word(i + 1, j, index + 1) or
            search_word(i - 1, j, index + 1) or
            search_word(i, j + 1, index + 1) or
            search_word(i, j - 1, index + 1)
        )

        # Backtrack: restore the original value of the cell
        board[i][j] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if search_word(i, j, 0):
                return True

    return False


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(exist(board, word))  # Output: True
