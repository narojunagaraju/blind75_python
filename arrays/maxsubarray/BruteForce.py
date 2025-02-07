# TC  O(n^2)
# SC O(1)

from typing import List


def max_subarray(nums: List[int]) -> int:
    n = len(nums)
    ans = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            ans = max(ans, current_sum)
    return ans


input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(input))
