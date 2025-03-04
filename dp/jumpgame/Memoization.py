# TC O(n^2)
# SC O(n)

def can_jump(nums: list[int]) -> bool:
    dp = [False] * len(nums)
    return helper(nums, 0, dp)


def helper(nums: list[int], i: int, dp: list[bool]) -> bool:
    if i >= len(nums) - 1:
        return True

    if dp[i]:  # if already visited return false
        return False

    dp[i] = True
    jump = nums[i]

    if jump == 0:
        return False

    for k in range(jump, 0, -1): ##params start,stop,step
        if helper(nums, i + k, dp):
            return True

    return False

print(can_jump([2, 3, 1, 1, 4]))
