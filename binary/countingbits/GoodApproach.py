# TC O(n)
# SC O(n)

def count_bits(n: int) -> list[int]:
    result = [0] * (n + 1)  # Including 0 to n

    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)

    return result

print(count_bits(2))