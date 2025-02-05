# TC O(n)
# SC O(n)

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    hash_set = set()

    for num in nums:
        if num in hash_set:
            return True
        else:
            hash_set.add(num)
    return False


print(contains_duplicate([1, 2, 3, 1]))
