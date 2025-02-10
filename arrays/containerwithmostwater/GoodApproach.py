# TC O(N)
# SC O(1)
from typing import List

def max_area(nums: List['int']) -> int:
    left, right = 0, len(nums) - 1
    max_water = float('-inf')

    while left < right:
        min_height = min(nums[left], nums[right])
        water = right - left
        max_water = max(max_water, min_height * water)
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return max_water

input_array = [1, 4, 2, 3]
print(max_area(input_array))
