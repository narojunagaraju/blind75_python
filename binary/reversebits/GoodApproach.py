
# SC O(1)

def reverse_bits(n: int) -> int:
    res = 0

    for i in range(32):
        lsb = n &  1
        revLsb = lsb << (31-i)
        res = res | revLsb
        n = n >> 1
    return res

print(reverse_bits(0b00000010100101000001111010011100))