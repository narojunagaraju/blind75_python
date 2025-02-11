# TC O(1)
# SC O(1)

def get_sum(a: int, b: int) -> int:
    return a if b == 0 else get_sum(a ^ b, (a & b) << 1)

print(get_sum(3, 2))