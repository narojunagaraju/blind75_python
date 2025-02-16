# TC O(n*m)
# SC O(n * m) + O(n + m)

def lcs(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)

    dp = [[-1] * m for _ in range(n)]

    return helper(s1, s2, n - 1, m - 1, dp)


def helper(s1: str, s2: str, i: int, j: int, dp: list[list[[int]]]) -> int:
    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j]:
        dp[i][j] = 1 + helper(s1, s2, i - 1, j - 1, dp)
    else:
        dp[i][j] = max(helper(s1, s2, i, j - 1, dp), helper(s1, s2, i - 1, j, dp))

    return dp[i][j]

s1 = "abcde"
s2 = "ace"
print(lcs(s1, s2))