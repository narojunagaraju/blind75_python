# TC O(b)
# SC O(1)

def get_sum(a: int, b: int) -> int:
    result = a
    for _ in range(b):
        result += 1
    return result


print(get_sum(3, 2))
