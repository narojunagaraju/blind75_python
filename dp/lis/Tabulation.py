# TC: O(N*N)
# SC: O(N*N)

from typing import List

def lis(input: List[int], n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for prev_index in range(i - 1, -2, -1):
            not_take = dp[i + 1][prev_index + 1]

            take = 0
            if prev_index == -1 or input[i] > input[prev_index]:
                take = 1 + dp[i + 1][i + 1]

            dp[i][prev_index + 1] = max(take, not_take)
    return dp[0][0]


print(lis([10, 9, 2, 5, 3, 7, 101, 18], 8))