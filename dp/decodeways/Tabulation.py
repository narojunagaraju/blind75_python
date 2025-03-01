# TC O(n)
# SC O(n)

def decode_ways(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n - 1, -1, -1):
        if s[i] != '0':
            dp[i] = dp[i + 1]
            if i < n - 1 and int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2]
    return dp[0]

print(decode_ways("12"))
