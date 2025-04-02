# TC: O(n^3)
# SC: O(1)

def min_window(s: str, t: str) -> str:
    min_len = float('inf')
    min_window = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            if contains_all_chars(sub_string, t) and len(sub_string) < min_len:
                min_len = len(sub_string)
                min_window = sub_string

    return min_window


def contains_all_chars(sub_string: str, t: str) -> bool:
    char_count = {}

    for char in sub_string:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char_count.get(char, 0) < t.count(char):
            return False

    return True

s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))
