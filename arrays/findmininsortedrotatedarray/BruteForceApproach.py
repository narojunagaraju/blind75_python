# TC O(N)
# SC O(1)
from typing import List

def find_min(nums: List['int']) -> int:
    for num in nums:
        if num < nums[0]:
            return num

    return nums[0]


sorted_list = [3, 4, 5, 1, 2]
print(find_min(sorted_list))
