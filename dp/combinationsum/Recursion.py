# TC O(2^n)
# SC O(target)

def combination_sum(nums, target):
    return helper(nums, len(nums) - 1, target)

def helper(nums, i, target):
    if i < 0:
        return 1 if target == 0 else 0

    if target == 0:
        return 1

    not_pick = helper(nums, i - 1, target)
    pick = 0
    if nums[i] <= target:
        pick = helper(nums, len(nums) - 1, target - nums[i])  # Reset to full size

    return not_pick + pick

# Example usage:
nums = [1, 2, 3]
target = 4
print(combination_sum(nums, target))  # Output: 3
