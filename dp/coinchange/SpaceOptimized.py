# TC O(N*T)
# SC O(T)

def min_elements(coins: list[int], amount: int) -> int:
    n = len(coins)

    prev = [0] * (amount + 1)
    cur = [0] * (amount + 1)

    # Initialize the first row
    for a in range(amount + 1):
        if a % coins[0] == 0:
            prev[a] = a // coins[0]
        else:
            prev[a] = int(1e9)

    # Fill the DP table using space optimization
    for i in range(1, n):
        for a in range(amount + 1):
            not_take = prev[a]
            take = int(1e9)
            if coins[i] <= a:
                take = 1 + cur[a - coins[i]]
            cur[a] = min(not_take, take)
        prev = cur[:]  # Copy cur to prev

    ans = prev[amount]
    return -1 if ans >= int(1e9) else ans

# Example usage
print(min_elements([1, 2, 5], 11))  # Output: 3
