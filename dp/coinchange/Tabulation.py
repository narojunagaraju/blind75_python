# TC O(N*T)
# SC O(N*T)

def coin_change(coins: list[int], amount: int) -> int:
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n)]

    for a in range(amount + 1):
        if a % coins[0] == 0:
            dp[0][a] = a // coins[0]
        else:
            dp[0][a] = int(1e9)

    for i in range(1, n):
        for a in range(amount + 1):
            not_take = dp[i - 1][a]
            take = int(1e9)
            if coins[i] <= a:
                take = 1 + dp[i][a - coins[i]]
            dp[i][a] = min(take, not_take)

    ans = dp[n - 1][amount]
    return -1 if ans >= int(1e9) else ans
