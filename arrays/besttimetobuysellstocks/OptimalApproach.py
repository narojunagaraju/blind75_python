# TC O(n)
# SC O(1)
from typing import List

def get_max_profit(prices: List[int]) -> int:
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


input_prices = [7, 1, 5, 3, 6, 4]
print(get_max_profit(input_prices))
