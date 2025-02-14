# TC O(n)
# SC O(1)

def climbing_stairs(n: int) -> int:
    if n <= 1:
        return 1

    first, second = 1, 1
    for _ in range(2, n + 1):
        first, second = second, first + second

    return second


# Example Usage:
print(climbing_stairs(4))  # Output: 5
