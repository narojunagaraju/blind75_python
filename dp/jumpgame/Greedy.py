# TC O(n)
# SC O(1)

def can_jump(nums: list[int]) -> bool:
    n = len(nums)
    last_pos = n - 1
    for k in range(n - 2, -1, -1):
        if k + nums[k] >= last_pos:  # Can reach or go beyond last_pos
            last_pos = k

    return last_pos == 0


print(can_jump([2, 3, 1, 1, 4]))

