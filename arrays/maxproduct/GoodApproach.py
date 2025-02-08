# Time Complexity: O(N)
# Auxiliary Space: O(1)

from typing import List

def max_product_array(nums: List[int]) -> int:
    max_product = nums[0]
    min_product = nums[0]
    res = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            temp = max_product
            max_product = min_product
            min_product = temp

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        res = max(res, max_product)
    return res


input_max = [2, 3, -2, 4]
print(max_product_array(input_max))
