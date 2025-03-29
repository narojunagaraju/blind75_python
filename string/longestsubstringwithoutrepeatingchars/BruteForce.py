# TC: O(n^3)
# SC: O(min(n, m))

def length_of_longest_substring(s: str) -> int:
    max_len = 0

    for i in range(len(s)):
        seen = set()
        length = 0

        for j in range(i, len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                length += 1
            else:
                break

            max_len = max(max_len, length)
    return max_len

print(length_of_longest_substring("abcabcbb"))
