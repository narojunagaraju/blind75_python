# TC O(n^2)
# SC O(1)

from typing import List

def get_max_profit(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(profit, max_profit)
    return max_profit

inputPrices = [7, 1, 5, 3, 6, 4]
print(get_max_profit(inputPrices))
