# TC O(N^2)
# SC O(3*k) k is the no.of triplets

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            sum_value = nums[left] + nums[right]

            if sum_value == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif sum_value < target:
                left += 1
            else:
                right -= 1

    return result

input_array = [-1, 0, 1, 2, -1, -4]
print(three_sum(input_array))