 # Time Complexity: O(N2)
 # Auxiliary Space: O(1)

from typing import List

def max_product_array(nums:List[int])->int:
    max_product = nums[0]

    for i in range(len(nums)):
        product = 1
        for j in range(i,len(nums)):
            product *= nums[j]
            max_product = max(product,max_product)
    return max_product


input_max = [2,3,-2,4]
print(max_product_array(input_max))