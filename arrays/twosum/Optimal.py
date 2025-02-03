#
#  Time complexity is o(n)
#  Space Complexity is 0(n)
#


def twosum(nums, target):
    res = [0, 0]
    num_map = {}

    for i in range(len(nums)):
        if target - nums[i] in num_map:
            res[1] = i
            res[0] = num_map[target - nums[i]]
            return res
        num_map[nums[i]] = i
    return res


numbers = [2, 7, 11, 15]
targetValue = 9
print(twosum(numbers, targetValue))
