# TC O(N)
# SC O(1)

def rob(nums: list[int]) -> int:
    n = len(nums)
    prev2 = 0
    prev = nums[0]


    for i in range(1,n):
        not_take = prev
        take = nums[i]
        if i > 1:
            take += prev2
        current = max(not_take,take)
        prev2 = prev
        prev = current

    return prev

input = [1, 2, 3, 1]
print(rob(input))