# TC O(2^N)
# SC O(N)

def rob(nums: list[int]) -> int:
    return helper(len(nums) - 1, nums)


def helper(i: int, nums: list[int]) -> int:
    if i == 0:
        return nums[0]

    if i < 0:
        return 0

    take = nums[i] + helper(i - 2, nums)
    not_take = 0 + helper(i - 1, nums)

    return max(not_take, take)


input = [1, 2, 3, 1]
print(rob(input))
