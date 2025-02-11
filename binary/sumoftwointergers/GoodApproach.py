# TC O(1)
# SC O(1)

def get_sum(a: int, b: int) -> int:
    while b != 0:
        sum_value = a ^ b  # XOR for sum without carry
        carry = (a & b) << 1  # AND for carry, shifted left
        a = sum_value
        b = carry
    return a

print(get_sum(3, 2))