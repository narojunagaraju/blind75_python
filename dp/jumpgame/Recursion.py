# TC O(2^n)
# SC O(n)

def can_jump(nums: list[int]) -> bool:
    return helper(nums, 0)


def helper(nums: list[int], i: int) -> bool:
    if i >= len(nums) - 1:
        return True

    if nums[i] == 0:
        return False

    jump = nums[i]
    res = False

    while jump > 0:
        res = res or helper(nums, i + jump)
        jump -= 1
    return res


print(can_jump([2, 3, 1, 1, 4])) 
