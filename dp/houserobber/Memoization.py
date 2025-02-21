# TC O(N)
# SC O(N)


def rob(nums: list[int]) -> int:
    n = len(nums)
    dp = [-1] * (n + 1)
    return helper(n - 1, nums, dp)


def helper(i: int, nums: list[int], dp: list[int]) -> int:
    if i == 0:
        return nums[0]

    if dp[i] != -1:
        return dp[i]

    if i < 0:
        return 0

    take = nums[i] + helper(i - 2, nums, dp)
    not_take = 0 + helper(i - 1, nums, dp)

    dp[i] = max(not_take, take)
    return dp[i]


input = [2,7,9,3,1]
print(rob(input))
