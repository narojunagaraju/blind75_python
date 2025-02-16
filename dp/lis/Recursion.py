# TC O(2^n)
# SC O(n)

def length_of_lis(nums: list[int]) -> int:
    return helper(nums, 0, -1)


def helper(nums: list[int], index: int, prev_index: int) -> int:
    if index == len(nums):
        return 0

    not_take = helper(nums, index + 1, prev_index)
    take = 0
    if prev_index == -1 or nums[index] > nums[prev_index]:
        take = 1 + helper(nums, index + 1, index)

    return max(not_take, take)


print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
