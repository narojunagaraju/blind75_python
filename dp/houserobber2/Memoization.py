# TC O(N)
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

    a = len(list1)
    b = len(list2)
    dp1 = [-1] * (a + 1)
    dp2 = [-1] * (b + 1)

    res1 = helper(list1, a - 1, dp1)
    res2 = helper(list2, b - 1, dp2)
    return max(res1, res2)


def helper(list: list[int], i: int, dp: list[int]) -> int:
    if i == 0:
        return list[0]

    if i < 0:
        return 0

    if dp[i] != -1:
        return dp[i]

    not_take = helper(list, i - 1, dp)
    take = list[i] + helper(list, i - 2, dp)

    dp[i] = max(not_take, take)

    return dp[i]

print(rob([2, 3, 2]))