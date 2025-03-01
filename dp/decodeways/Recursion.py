# TC O(2^n)
# SC O(n)

def decode_ways(s: str) -> int:
    return helper(s, 0)


def helper(s: str, i: int) -> int:
    if i == len(s):
        return 1

    if s[i] == '0':
        return 0

    single_char = helper(s, i + 1)
    double_char = 0
    if i < len(s) - 1 and int(s[i:i + 2]) <= 26:
        double_char = helper(s, i + 2)

    return single_char + double_char


print(decode_ways("12"))
