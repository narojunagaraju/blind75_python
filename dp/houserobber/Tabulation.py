# TC O(N)
# SC O(N)

def rob(nums: list[int]) -> int:
    n = len(nums)
    dp = [-1] * (n + 1)
    dp[0] = nums[0]

    for i in range(1, n):
        not_take = dp[i - 1]
        take = nums[i]
        if i > 1:
            take += dp[i - 2]
        dp[i] = max(not_take, take)
    return dp[n - 1]


input = [1, 2, 3, 1]
print(rob(input))
