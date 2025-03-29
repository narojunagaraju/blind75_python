# TC: O(n)
# SC: O(min(n, m))

def length_of_longest_substring(s: str) -> int:
    seen = set()
    i = 0
    j = 0
    maxLen = 0

    while j < len(s):
        if s[j] not in seen:
            seen.add(s[j])
            maxLen = max(maxLen, j - i + 1)
            j += 1
        else:
            seen.remove(s[i])
            i += 1
    return maxLen

print(length_of_longest_substring("abcabcbb"))
