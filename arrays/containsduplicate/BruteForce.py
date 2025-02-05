# TC O(n^2)
# SC O(1)

from typing import List

def contains_duplicate(nums: List[int]) -> int:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(contains_duplicate([1,2,3,1]))