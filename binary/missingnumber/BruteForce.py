# TC O(n^2)
# SC O(1)

def missing_number(nums: list[int]) -> int:
    n = len(nums)
    for i in range(n + 1):
        if i not in nums:
            return i
    return -1  # If no missing number is found

print(missing_number([3,0,1]))