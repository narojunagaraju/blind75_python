# TC O(n^2)
# SC O(n)

def can_jump(nums: list[int]) -> bool:
    n = len(nums)
    dp = [False] * n
    dp[-1] = True  # the last index is always reachable

    for k in range(n - 2, -1, -1):
        furthest_jump = min(k + nums[k], n - 1)
        for j in range(k + 1, furthest_jump + 1):
            if dp[j]:
                dp[k] = True
                break

    return dp[0]

print(can_jump([2, 3, 1, 1, 4]))
