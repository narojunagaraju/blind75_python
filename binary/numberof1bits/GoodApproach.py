# TC O(number of set bits)
# SC O(1)
def count_bits(num: int) -> int:
    count = 0

    while num != 0:
        num = num & (num - 1)
        count += 1

    return count

print(count_bits(11))