# TC O(N*T)
# SC O(N*T) + O(N)

def coin_change(coins: list[int], amount: int) -> int:
    n = len(coins)
    dp = [[-1] * (amount + 1) for _ in range(n)]

    ans = helper(n - 1, coins, amount, dp)
    return -1 if ans >= int(1e9) else ans


def helper(n: int, coins: list[int], amount: int, dp: list[list[int]]) -> int:
    if n == 0:
        return amount // coins[0] if amount % coins[0] == 0 else int(1e9)

    if dp[n][amount] != -1:
        return dp[n][amount]

    not_take = helper(n - 1, coins, amount, dp)
    take = int(1e9)

    if coins[n] <= amount:
        take = 1 + helper(n, coins, amount - coins[n], dp)

    dp[n][amount] = min(not_take,take)
    return dp[n][amount]


coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))
