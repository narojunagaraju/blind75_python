# TC O(2^(n+m))
# SC O(n + m)

def lcs(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)

    return helper(s1, s2, n - 1, m - 1)


def helper(s1: str, s2: str, i: int, j: int) -> int:
    if i < 0 or j < 0:
        return 0

    if s1[i] == s2[j]:
        return 1 + helper(s1, s2, i - 1, j - 1)
    else:
        return max(helper(s1, s2, i - 1, j), helper(s1, s2, i, j - 1))


s1 = "abcde"
s2 = "ace"
print(lcs(s1, s2))
