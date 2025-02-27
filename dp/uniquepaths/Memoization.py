# TC O(M*N)
# SC O((N-1)+(M-1)) + O(M*N)

def count_ways(m: int, n: int) -> int:
    dp = [[-1] * n for _ in range(m)]
    return helper(m - 1, n - 1, dp)


def helper(i: int, j: int, dp: list[list[int]]) -> int:
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    up = helper(i - 1, j, dp)
    left = helper(i, j - 1, dp)

    dp[i][j] = up + left
    return dp[i][j]

print(count_ways(3, 2))
