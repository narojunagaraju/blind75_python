# TC O(n)
# SC O(min(n, m))

def character_replacement(s: str, k: int) -> int:
    char_count = {}
    max_length = 0
    max_repeat_count = 0
    start = 0

    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        max_repeat_count = max(max_repeat_count, char_count[s[end]])

        if end - start + 1 - max_repeat_count > k:
            char_count[s[start]] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

s = "ABAB"
k = 2
print(character_replacement(s, k))
