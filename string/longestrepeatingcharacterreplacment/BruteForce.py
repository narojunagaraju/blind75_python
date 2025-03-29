# TC O(n^3)
# SC O(1)

def character_replacement(s: str, k: int) -> int:
    max_length = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            max_char_count = max(substring.count(c) for c in set(substring))
            replacement_needed = len(substring) - max_char_count

            if replacement_needed <= k:
                max_length = max(max_length, len(substring))

    return max_length


s = "ABAB"
k = 2
print(character_replacement(s, k))
