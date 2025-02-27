# TC O(2^(m+n))
# SC O(m+n)

def count_ways(m: int, n: int) -> int:
    return helper(m - 1, n - 1)


def helper(i: int, j: int) -> int:
    if i == 0 and j == 0:
        return 1

    if i < 0 or j < 0:
        return 0

    up = helper(i - 1, j)
    left = helper(i, j - 1)

    return up + left


print(count_ways(3, 2))
