# TC O(2^n)
# SC O(n^2) + O(n)

def length_of_lis(nums: list[int]) -> int:
    n = len(nums)
    dp = [[-1] * n for _ in range(n)]
    return lis_helper(nums, 0, -1, dp)

def lis_helper(nums: list[int], index: int, prev_index: int, dp: list[list[int]]) -> int:
    if index == len(nums):
        return 0

    if prev_index != -1 and dp[index][prev_index] != -1:
        return dp[index][prev_index]

    not_take = lis_helper(nums, index + 1, prev_index, dp)
    take = 0
    if prev_index == -1 or nums[index] > nums[prev_index]:
        take = 1 + lis_helper(nums, index + 1, index, dp)

    if prev_index != -1:
        dp[index][prev_index] = max(not_take, take)
        return dp[index][prev_index]

    return max(take, not_take)

print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
