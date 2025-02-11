# TC O(n * sizeof(int))
# SC O(n)

def count_bits(n: int) -> list[int]:
    result = [0] * (n + 1)

    for i in range(n + 1):
        result[i] = bin(i).count('1')

    return result

print(count_bits(2))
