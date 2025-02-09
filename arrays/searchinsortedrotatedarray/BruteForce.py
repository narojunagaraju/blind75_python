# TC O(N)
# SC O(1)

from typing import List


def search(nums: List['int'], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


numbers = [4, 5, 6, 7, 0, 1, 2]
print(search(numbers, 0))
