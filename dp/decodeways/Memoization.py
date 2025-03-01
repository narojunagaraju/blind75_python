# TC O(n)
# SC O(n)

def decode_ways(s: str) -> int:
    dp = [-1] * (len(s) + 1)
    return helper(s, 0, dp)


def helper(s: str, i: int, dp: list) -> int:
    if i == len(s):
        return 1

    if s[i] == '0':
        return 0

    if dp[i] != -1:
        return dp[i]

    single_char = helper(s, i + 1, dp)
    double_char = 0
    if i < len(s)-1 and int(s[i:i + 2]) <= 26:
        double_char = helper(s, i + 2, dp)

    dp[i] = single_char + double_char
    return dp[i]

print(decode_ways("12"))
