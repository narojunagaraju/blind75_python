#
#  Time complexity is o(n^2)
#  Space complexity is o(1)
#

def twosum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result
    return result


numbers = [2, 7, 11, 15]
targetValue = 9
print(twosum(numbers, targetValue))
