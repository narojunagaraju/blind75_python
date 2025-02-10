# TC O(N)
# SC O(1)

from typing import List

def max_area(height: List[int]) -> int:
    max_water = 0
    left, right = 0, len(height) - 1

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_water = max(max_water, h * w)

        # Move pointers based on the shorter height to potentially find a larger area.
        if height[left] < height[right]:
            current_left = left
            while current_left < right and height[current_left] <= height[left]:
                current_left += 1
            left = current_left
        else:
            current_right = right
            while current_right > left and height[current_right] <= height[right]:
                current_right -= 1
            right = current_right

    return max_water

input_array = [1, 4, 2, 3]
print(max_area(input_array))