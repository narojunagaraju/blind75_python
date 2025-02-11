# TC O(n)
# SC O(1)

def missing_number(nums: list[int]) -> int:
    n = len(nums)
    result = n
    for i in range(n):
        result ^= i ^ nums[i]
    return result

nums = [3, 0, 1]
print(missing_number(nums))
