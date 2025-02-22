# TC O(2^N)
# SC O(N)

def rob(nums: list[int]) -> int:
    list1 = []
    list2 = []
    n = len(nums)

    for i in range(n):
        if i != 0:
            list1.append(nums[i])
        if i != (n - 1):
            list2.append(nums[i])

    res1 = helper(list1, len(list1) - 1)
    res2 = helper(list2, len(list2) - 1)

    return max(res1, res2)


def helper(list: list[int], i: int) -> int:
    if i == 0:
        return list[0]

    if i < 0:
        return 0

    not_take = 0 + helper(list, i - 1)
    take = list[i] + helper(list, i - 2)

    return max(not_take, take)


print(rob([2, 3, 2]))
