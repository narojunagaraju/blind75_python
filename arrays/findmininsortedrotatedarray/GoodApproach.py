# TC O(log N)
# SC O(1)

from typing import List

def find_min(nums: List['int']) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

sorted_list = [3, 4, 5, 1, 2]
print(find_min(sorted_list))