# TC O(n)
# SC O(1)

def max_sub_array(input):
    n = len(input)
    max_sum = float('-inf')  # Set initial max to negative infinity
    current_sum = 0

    for i in range(n):
        current_sum += input[i]
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0  # Reset current sum if it's negative

    return max_sum

input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(input))