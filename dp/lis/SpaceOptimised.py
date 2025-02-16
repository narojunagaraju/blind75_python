# TC: O(N*N)
# SC: O(N)


def lis(input: list[int], n: int) -> int:
    next_dp = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(n - 1, -1, -1):  # Iterating from n-1 to 0 (reverse order)
        for prev_index in range(i - 1, -2, -1):  # Iterating from i-1 to -1 (inclusive)
            not_take = 0 + next_dp[prev_index + 1]

            take = 0
            if prev_index == -1 or input[i] > input[prev_index]:
                take = 1 + next_dp[i + 1]

            curr[prev_index + 1] = max(not_take, take)

        next_dp = curr[:]  # Clone the current dp to next_dp

    return curr[0]

print(lis([10, 9, 2, 5, 3, 7, 101, 18], 8))