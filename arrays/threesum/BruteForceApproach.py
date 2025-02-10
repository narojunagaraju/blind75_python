# TC O(N^3)
# SC O(3*k) k is the no.of triplets

from typing import List

def three_sum(nums: List['int']) -> list[list[int]]:
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in result:
                        result.append(triplet)

    return result


input_array = [-1, 0, 1, 2, -1, -4]
print(three_sum(input_array))
