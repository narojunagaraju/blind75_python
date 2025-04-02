# TC: O(n)
# SC: O(min(n, m))

def min_window(s: str, t: str) -> str:
    from collections import Counter

    target_char_count = Counter(t)
    window_char_count = {}

    left = 0
    min_len = float('inf')
    min_window = ""
    required_chars = len(target_char_count)
    formed_chars = 0

    for right, char in enumerate(s):
        window_char_count[char] = window_char_count.get(char, 0) + 1

        if window_char_count[char] == target_char_count[char]:
            formed_chars += 1

        while formed_chars == required_chars:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]

            left_char = s[left]
            window_char_count[left_char] -= 1

            if left_char in target_char_count and window_char_count[left_char] < target_char_count[left_char]:
                formed_chars -= 1

            left += 1

    return min_window


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(min_window(s, t))
