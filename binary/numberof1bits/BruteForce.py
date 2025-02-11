# TC O(b)
# SC O(1)

def count_bits(num: int) -> int:
    count = 0

    while num != 0:
        count += num & 1
        num >>= 1

    return count

print(count_bits(11))