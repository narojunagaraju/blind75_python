# TC o(2^n)
# SC o(n)

def coin_change(coins: list[int], amount: int) -> int:
    ans = helper(len(coins) - 1, coins, amount)
    return -1 if ans >= int(1e9) else ans


def helper(n: int, coins: list[int], amount: int) -> int:
    if n == 0:
        return amount // coins[0] if amount % coins[0] == 0 else int(1e9)

    not_take = helper(n - 1, coins, amount)
    take = int(1e9)
    if coins[n] <= amount:
        take = 1 + helper(n, coins, amount - coins[n])
    return min(take, not_take)


coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))
