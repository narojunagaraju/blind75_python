# TC O(N^2)
# SC O(1)
from typing import List

def max_area(nums: List['int']) -> List['int']:
    max_water = float('-inf')

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            height = min(nums[i], nums[j])
            water = j - i
            max_water = max(max_water, height * water)
    return max_water


input_array = [1, 4, 2, 3]
print(max_area(input_array))
