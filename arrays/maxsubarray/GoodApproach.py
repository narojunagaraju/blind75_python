# TC  O(n log n)
# SC O(n log n)

def max_sub_array_divide_conquer(nums):
    return max_sub_array_helper(nums, 0, len(nums) - 1)

def max_sub_array_helper(nums, left, right):
    if left == right:
        return nums[left]

    mid = left + (right - left) // 2

    left_max = max_sub_array_helper(nums, left, mid)
    right_max = max_sub_array_helper(nums, mid + 1, right)
    cross_max = max_crossing_sub_array(nums, left, mid, right)

    return max(left_max, right_max, cross_max)


def max_crossing_sub_array(nums, left, mid, right):
    left_sum = float('-inf')
    current_sum = 0

    # Calculate left maximum sum
    for i in range(mid, left - 1, -1):
        current_sum += nums[i]
        left_sum = max(left_sum, current_sum)

    right_sum = float('-inf')
    current_sum = 0

    # Calculate right maximum sum
    for i in range(mid + 1, right + 1):
        current_sum += nums[i]
        right_sum = max(right_sum, current_sum)

    return left_sum + right_sum

input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array_divide_conquer(input))