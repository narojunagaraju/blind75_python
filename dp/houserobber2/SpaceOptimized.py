# TC O(N)
# SC O(1)

def rob(nums: list[int]) -> int:
    list1 = []
    list2 = []
    n = len(nums)

    for i in range(n):
        if i != 0:
            list1.append(nums[i])

        if i != (n - 1):
            list2.append(nums[i])


    res1 = helper(list1)
    res2 = helper(list2)

    return max(res1, res2)


def helper(list: list[int]) -> int:
    prev2 = 0
    prev1 = list[0]

    for i in range(1, len(list)):
        not_take = prev1
        take = list[i]
        if i > 1:
            take += prev2

        current = max(not_take,take)
        prev2 = prev1
        prev1 = current

    return prev1

print(rob([2, 3, 2]))
