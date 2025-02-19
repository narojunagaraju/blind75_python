# TC O(2^n)
# SC O(target)

def combination_sum(nums, target):
    n = len(nums)
    dp = [[-1] * (target + 1) for _ in range(n)]
    return combination_sum_helper(nums, n - 1, target, dp)


def combination_sum_helper(nums, index, target, dp):
    if index < 0:
        return 1 if target == 0 else 0

    if target == 0:
        return 1

    if dp[index][target] != -1:
        return dp[index][target]

    not_pick = combination_sum_helper(nums, index - 1, target, dp)
    pick = 0
    if nums[index] <= target:
        pick = combination_sum_helper(nums, len(nums) - 1, target - nums[index], dp)

    dp[index][target] = pick + not_pick
    return dp[index][target]

nums = [1, 2, 3]
target = 4
print(combination_sum(nums, target))