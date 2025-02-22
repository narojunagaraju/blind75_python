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

    dp1 = [0] * (a + 1)
    dp2 = [0] * (b + 1)
    dp1[0] = list1[0]
    dp2[0] = list2[0]

    res1 = helper(list1, dp1)
    res2 = helper(list2, dp2)

    return max(res1, res2)


def helper(list: list[int], dp: list[int]) -> int:
    for i in range(1, len(list)):
        not_take = dp[i - 1]
        take = list[i]
        if i > 1:
            take += dp[i - 2]

        dp[i] = max(not_take,take)

    return dp[len(list)-1]

print(rob([2, 3, 2]))
