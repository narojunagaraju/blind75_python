# Time Complexity: O(N)
# Auxiliary Space: O(1)

from typing import List


def max_product_array(nums: List[int]) -> int:
    n = len(nums)
    max_ending_here = nums[0]
    min_ending_here = nums[0]
    max_so_far = nums[0]

    for i in range(1, n):
        temp = max(nums[i], nums[i] * max_ending_here, nums[i] * min_ending_here)
        min_ending_here = min(nums[i], nums[i] * max_ending_here, nums[i] * min_ending_here)
        max_ending_here = temp
        max_so_far = max(max_so_far,max_ending_here)

    return max_so_far

input_max = [2, 3, -2, 4]
print(max_product_array(input_max))
