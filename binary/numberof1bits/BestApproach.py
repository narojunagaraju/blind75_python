# TC O(1)
# SC O(1)

def count_bits(number: int) -> int:
    return bin(number).count('1')

print(count_bits(11))