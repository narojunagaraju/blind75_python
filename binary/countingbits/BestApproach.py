# TC O(n * sizeof(int))
# SC O(n)

def count_bits(n: int) -> list[int]:
    return [bin(i).count('1') for i in range(n + 1)]

print(count_bits(2))