# TC O(log N)
# SC O(1)

from typing import List

def search(nums: List['int'], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:  # if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target <= nums[right]:  # if target > nums[mid] and target <= nums[right]
                left = mid + 1
            else:
                right = mid - 1

    return -1

numbers = [4, 5, 6, 7, 0, 1, 2]
print(search(numbers, 0))
