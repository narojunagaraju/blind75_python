# TC: O(n)
# SC: O(min(n, m))

def min_window(s: str, t: str) -> str:
    char_count = {}
    for char in t:
        char_count[char] = char_count.get(char, 0) + 1

    left = 0
    min_len = float('inf')
    min_window = ""

    required_chars = len(char_count)
    formed_chars = 0

    for right in range(len(s)):
        char = s[right]

        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                formed_chars += 1

        while formed_chars == required_chars:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]

            left_char = s[left]
            if left_char in char_count:
                char_count[left_char] += 1
                if char_count[left_char] > 0:
                    formed_chars -= 1

            left += 1

    return min_window



s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))