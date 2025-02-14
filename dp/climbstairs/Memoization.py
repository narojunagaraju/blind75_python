# TC O(2^n)
# SC O(n)

def climb_stairs(n: int, dp: list) -> int:
    if n == 1 or n == 0:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = climb_stairs(n - 1, dp) + climb_stairs(n - 2, dp)
    return dp[n]


# Example Usage:
n = 4  # Change this value as needed
dp = [-1] * (n + 1)
print(climb_stairs(n, dp))
