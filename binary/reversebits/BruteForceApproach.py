# TC O(32)
# SC O(1)

def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

print(reverse_bits(0b00000010100101000001111010011100))